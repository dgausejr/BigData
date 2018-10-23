# Projeto Big Data - Uniasselvi - outubro / 2018
# Dionisio Gause Junior
# Missão: Implementar o metodo kNN para a flor IRIS
# Desenvolimento: Baseado na aula do professor Sanderson Macedo
# Disponível em: https://www.youtube.com/watch?v=cCMi1fjfAUY

#Importando bibliotecas necessárias

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# carrega dados em dataframe df

df = pd.read_csv('iris.csv')

# usado para identificar o nome das colunas
print(df.columns)

# usado para visualizar os dados
print(df)

# print usado para descrição dos dados
print(df.describe())

# Usado para visualizar a dispersão dos dados
sb.pairplot(df, hue='Species')
plt.show()

# selecionando as caracteristicas para a classificação em um array
X = np.array(df.drop('Species', 1))

# visualizar os dados do array criado (X)
print(X)

# selecionando a classes para classificação em array
y = np.array(df.Species)

# visualizar os dados do array criado(y)
print(y)

# importando a funcao KNeighborsClassifier da biblioteca sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# informando o n_neighbors a verificar - quanto maior, maior a probabilidade de acerto
# sempre em valores impares (evitando empate na classificação)
knn = KNeighborsClassifier(n_neighbors=5)

# Treinando um classificador com base nas caracteristicas (X) e classe (y)
knn.fit(X, y)

comp_sepala = float(input('Digite o comprimento da Sépala: '))
larg_sepala = float(input('Digite a largura da Sépala....: '))
comp_petala = float(input('Digite o comprimento da Pétala: '))
larg_petala = float(input('Digite a largura da Pétala....: '))

p = knn.predict([[comp_sepala, larg_sepala, comp_petala, larg_petala]])

print(f'Com base nos dados informados e utilizando o método K-NN, é provável que seja uma Iris {p}\n'
      f'Obrigado por utilizar nosso APP, volte sempre !')