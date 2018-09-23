import pandas as pd
import numpy as np
from math import sqrt

avaliacoes = {'Ana':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Norbit': 2.5,
                   'Star Wars': 3.0},

              'Marcos':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 1.5,
                   'Exterminador do Futuro': 5.0,
                   'Star Wars': 3.0,
                   'Norbit': 3.5},

              'Pedro':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Star Wars': 4.0},

              'Claudia':
                  {'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Star Wars': 4.5,
                   'Exterminador do Futuro': 4.0,
                   'Norbit': 2.5},

              'Adriano':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Trek': 2.0,
                   'Exterminador do Futuro': 3.0,
                   'Star Wars': 3.0,
                   'Norbit': 2.0},

              'Janaina':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Wars': 3.0,
                   'Exterminador do Futuro': 5.0,
                   'Norbit': 3.5},

              'Leonardo':
                  {'O Ultimato Bourne': 4.5,
                   'Norbit': 1.0,
                   'Exterminador do Futuro': 4.0}
              }



def euclidiana(usuarioA, usuarioB):
    si = {}
    for item in avaliacoes[usuarioA]:
        if item in avaliacoes[usuarioB]: si[item] = 1

    if len(si) == 0:
        return 0

    soma = sum([pow(avaliacoes[usuarioA][item] - avaliacoes[usuarioB][item], 2)
               for item in avaliacoes[usuarioA] if item in avaliacoes[usuarioB]])
    return 1/(1 + sqrt(soma))

def getSimilaridade(usuario):
    similares = [(euclidiana(usuario, outro), outro)
                 for outro in avaliacoes if outro != usuario]
    similares.sort()
    similares.reverse()
    return similares

for usuario in avaliacoes:
    print(usuario + "\r\n")
    print(getSimilaridade(usuario))