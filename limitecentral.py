'''
Demonstração do Teorema do Limite Central utilizando 3 gráficos
*Os parâmetros podem ser alterados para melhor visualização das alterações que os gráficos sofrem com diferentes quantidades de dados
Autor: Alef Matias
'''

import random
from collections import Counter
import matplotlib.pyplot as plt
plt.style.use('dark_background')


# Gerar a média de uma lista
def mediaLista(lista):
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    return media


# Gerar uma lista no intervalo de 1 até um valor escolhido
def gerarLista(quantidade_dados):
    lista = []
    for i in range(1, quantidade_dados + 1):
        lista.append(i)
    return lista


# Retirar uma quantidade de amostras de uma determinada lista
def gerarAmostras(lista, quantidade_amostras):
    amostra = []
    for rodadas in range(quantidade_amostras):
        amostra.append(random.randrange(1, len(lista) + 1, 1))
    return amostra


# Gera uma lista com a média das amostras geradas partindo dos parâmetros das outras funções
def gerarMedias(quantidade_medias, quantidade_dados, quantidade_amostras):
    lista_mestre = []
    for i in range(quantidade_medias):
        lista_mestre.append(mediaLista(gerarAmostras(gerarLista(quantidade_dados), quantidade_amostras)))
    return lista_mestre


medias = gerarMedias(10000, 10, 4)
medias2 = gerarMedias(10000, 15, 6)
medias3 = gerarMedias(10000, 20, 8)

# Fazendo a contagem de quantas vezes uma média se repetiu na lista
x = Counter(medias).keys()
y = Counter(medias).values()
x2 = Counter(medias2).keys()
y2 = Counter(medias2).values()
x3 = Counter(medias3).keys()
y3 = Counter(medias3).values()

# Gerando os 3 gráficos juntos com intervalos diferentes
plt.bar(x, y, color='lightseagreen', alpha=0.7)
plt.annotate('Intervalo de 1 a 20', xy=(10, 280))
plt.annotate('Intervalo de 1 a 15', xy=(7.5, 420))
plt.annotate('Intervalo de 1 a 10', xy=(5, 690))
plt.bar(x2, y2, color='peachpuff', alpha=0.7)
plt.bar(x3, y3, color='lightcoral', alpha=0.7)
plt.title('Teorema do Limite Central')
plt.xlabel('Médias')
plt.ylabel('Quantidade')
plt.show()
