from PIL import Image
from time import time
import numpy as np


def totuple(a):
    # Função totuple - serve para transformar um array em uma tupla
    # Funciona de forma recursiva então é possível transformar vários arrays
    # aninhados, como é o caso.
    # Créditos: Bi Rico - https://qastack.com.br/programming/10016352/convert-numpy-array-to-tuple
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a


# Abrindo imagem e gerando array de rgb dos bits
img = Image.open('meteor_challenge_01.png')
data = np.asarray(img)

# Convertemos o array para tuplas pois é mais fácil de realizar comparações
# Fazemos a conversão de toda a matriz pois é mais eficiente do que converter
# toda vez que for utilizar
tupleData = totuple(data)

# Definição das cores de comparação do programa
# Usamos tuplas para evitar problemas de comparação com vetores
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red = (255, 0, 0, 255)
blue = (0, 0, 255, 255)

# Vetor usado para gravar as colunas que possuem bits de água
waterCols = []

# Variáveis que salvam o indice do nível do chão e da água
groundLvl = -1
waterLevel = -1

# Contadores
meteors = 0
stars = 0
fallOnWater = 0

# Salvando largura e comprimento da matriz
h, w, _ = data.shape

# Encontra o nível do chão
# Fizemos aqui uma estimativa pois ao observar a imagem percebemos que próximo ao centro
# possuímos um nível mais alto de chão podendo cortar mais iterações
start = time()
wcentro = int(w/2)
for i in range(0, h):
    if(tupleData[i][wcentro] == black):
        groundLvl = i
        break

# Encontra o nível da água
for i in range(0, w):
    if(waterLevel != -1):
        break
    for j in range(int(h/2), h):
        if(tupleData[j][i] == blue):
            waterLevel = j
            break

# Encontra colunas em que há bits com água
for i in range(0, w):
    if(tupleData[waterLevel][i] == blue):
        waterCols.append(i)


# Itera para contar quantidade de estrelas e meteoros
# Usa o nível do chão para parar de iterar pois a partir do chão não há mais estrelas
# Quando encontra um meteoro verifica se o indice de sua coluna está contido no array
# com os indices de coluna que contém água, se sim significa que o meteoro vai cair na água
for i in range(0, groundLvl):
    for j in range(0, w):
        if(tupleData[i][j] == red):
            meteors += 1
            if(j in waterCols):
                fallOnWater += 1
        if(tupleData[i][j] == white):
            stars += 1

end = time()

# Exibe os resultados
print("O número de meteoros encontrados foi: ", meteors)
print("O número de estrelas encontradas foi: ", stars)
print("O número de meteoros que cairão na água é: ", fallOnWater)
print("Tempo de processamento: ", end - start)
