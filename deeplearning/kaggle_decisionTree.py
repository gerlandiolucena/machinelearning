from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

melb_data = pd.read_csv("datasources/melb_data.csv")

melb_data.describe()

melb_data = melb_data.dropna(axis=0)

y = melb_data.Price

melb_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melb_data[melb_features]

X.describe()

X.head()

melb_model = DecisionTreeRegressor(random_state=1)

melb_model.fit(X, y)

print(melb_model.predict(X.head()))
print(y.head())

predicted_home_prices = melb_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

iowa_model = DecisionTreeRegressor(random_state=0)
iowa_model.fit(train_X, train_y)

val_predictions = melb_model.predict(val_X)

print(val_predictions[0:5])
print(val_y.head())

val_mae = mean_absolute_error(val_predictions, val_y)
print(val_mae)
print("Validation MAE: {:,.0f}" . format(val_mae))

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

for max_leaf_nodes in [5, 25, 50, 100, 250, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d, Mae: %d" % (max_leaf_nodes, my_mae))

final_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=0)
final_model.fit(train_X, train_y)