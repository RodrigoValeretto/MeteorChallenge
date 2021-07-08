from PIL import Image
import numpy as np

# Abrindo imagem e gerando array de rgb dos bits
img = Image.open('meteor_challenge_01.png')
data = np.asarray(img)

# Definição das cores de comparação do programa
# Usamos tuplas para evitar problemas de comparação com vetores
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red = (255, 0, 0, 255)
blue = (0, 0, 255, 255)

# Vetor usado para gravar coordenadas dos possíveis meteoros
coords = []
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
wcentro = int(w/2)
for i in range(0, h):
    if(tuple(data[i, wcentro]) == black):
        groundLvl = i
        break

# Encontra o nível da água
for i in range(0, h):
    if(waterLevel != -1):
        break
    for j in range(0, w):
        if(tuple(data[i, j]) == blue):
            waterLevel = i
            break

# Encontra colunas em que há bits com água
for i in range(0, w):
    if(tuple(data[waterLevel, i]) == blue):
        waterCols.append(i)


# Itera para contar quantidade de estrelas e meteoros
# Usa o nível do chão para parar de iterar pois a partir do chão não há mais estrelas
for i in range(0, groundLvl):
    for j in range(0, w):
        if(tuple(data[i, j]) == red):
            meteors += 1
            coords.append((i, j))
        if(tuple(data[i, j]) == white):
            stars += 1

# itera para verificar a trajetória dos meteoros e ver se atingem a terra
# Usa o vetor de colunas de bits de água para verificar se algum dos meteoros possui
# o indice da coluna igual a um indice desse vetor, se sim significa que ele vai cair
# ná água.
for i in coords:
    if(i[1] in waterCols):
        fallOnWater += 1

# Exibe os resultados
print("O número de meteoros encontrados foi: ", meteors)
print("O número de estrelas encontradas foi: ", stars)
print("O número de meteoros que cairão na água é: ", fallOnWater)
