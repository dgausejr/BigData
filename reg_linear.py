# Projeto Big Data - Uniasselvi - outubro / 2018
# Dionisio Gause Junior
# Desafio: Implementar o metodo de regressão linear simples
# Referências:
# https://www.youtube.com/watch?v=gzyq_6wdtSk
# https://medium.com/@felipebormann/aprendendo-scikit-learn-e-um-pouco-mais-de-python-6b27025f9d5b
# http://neylsoncrepalde.github.io/2018-02-25-regressao-linear-python/
# https://imasters.com.br/back-end/data-science-regressoes-com-python


# importação das bibliotecas a serem utilizadas

import numpy as np
import matplotlib.pyplot as plt

# Criando os arrays com as variáveis x e y a serem utilizados

km_percorridos = [8, 10, 12,16,20]
x = np.array(km_percorridos)

calorias_queimadas = [90, 112, 148, 189, 212]
y = np.array(calorias_queimadas)

# chama a função polyfit informando os vetores e o grau do polinomio
# onde a regressão linear o grau é 1 - equação da reta

p1 = np.polyfit(x, y, 1)

# a partir dos coeficientes linear e angular calcula-se o y predito

yfit = p1[0] * x + p1[1]

# a seguir calcula-se o resíduo (valor de y menos o predito)

yresid = y - yfit

# Calcula-se o somatório dos quadrados dos residuos

SQresid = sum(pow(yresid,2))

# Calcula-se o somatório da diferença entre o valor real e a média dos valores de y
# quantidade de elementos de y vezes a variança

SQtotal = len(y) * np.var(y)

# com base nos valores SQresid e SQtotal calcula-se o coeficiente de determinação

R2 = 1 - SQresid/SQtotal

# mostra o intercepto e inclinação
print(f'\nCoeficiente angular = {p1[0]}\n')
print(f'Coeficiente linear = {p1[1]}\n')

# mostra o coeficiente de determinação
print(f'Coeficiente de Determinação = {R2}')

# determina-se as variáveis para apresentção do gráfico (plt)
plt.title('Quantidade de km percorridos por calorias queimadas') #título do gráfico
plt.xlabel('“Km percorridos') #Legenda na horizontal
plt.ylabel('Calorias Queimadas') #Legenda do eixo Y
plt.plot(x, y, 'o') # os dados nos dois eixos

# valores preditos de y (linha)

plt.plot(x, np.polyval(p1,x),'g--')
plt.grid(True) # Grid = grades, zonas do gráfico
plt.show() # mostra o gráfico