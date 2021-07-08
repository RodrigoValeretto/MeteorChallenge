from PIL import Image
import numpy as np

# Abrindo imagem e gerando array de rgb dos bits
img = Image.open('meteor_challenge_01.png')
data = np.asarray(img)

# Definição das cores de comparação do programa
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
red = (255, 0, 0, 255)
blue = (0, 0, 255, 255)

# Vetor usado para gravar coordenadas dos possíveis meteoros
coords = []
waterCols = []

groundLvl = -1
waterLevel = -1

# Contadores
meteors = 0
stars = 0
fallOnWater = 0

# Salvando largura e comprimento da matriz
h, w, _ = data.shape

for i in range(0, h):
    if(tuple(data[i, 352]) == black):
        groundLvl = i
        break

for i in range(0, h):
    if(waterLevel != -1):
        break
    for j in range(0, w):
        if(tuple(data[i, j]) == blue):
            waterLevel = i
            break


for i in range(0, w):
    if(tuple(data[waterLevel, i]) == blue):
        waterCols.append(i)


# Itera para contar quantidade de estrelas e meteoros
for i in range(0, groundLvl):
    for j in range(0, w):
        if(tuple(data[i, j]) == red):
            meteors += 1
            coords.append((i, j))
        if(tuple(data[i, j]) == white):
            stars += 1

# itera para verificar a trajetória dos meteoros e ver se atingem a terra
for i in coords:
    if(i[1] in waterCols):
        fallOnWater += 1

print("O número de meteoros encontrados foi: ", meteors)
print("O número de estrelas encontradas foi: ", stars)
print("O número de meteoros que cairão na água é: ", fallOnWater)
