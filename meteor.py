from PIL import Image
from time import time
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

# Contadores
meteors = 0
stars = 0
fallOnWater = 0

# Salvando largura e comprimento da matriz
w, h, _ = data.shape

start = time()
# Itera para contar quantidade de estrelas e meteoros
for i in range(0, h):
    for j in range(0, w):
        if(tuple(data[i, j]) == red):
            meteors += 1
            coords.append((i, j))
        if(tuple(data[i, j]) == white):
            stars += 1

# itera para verificar a trajetória dos meteoros e ver se atingem a terra
fallCols = set()
for i in coords:
    for j in range(i[0], h):
        if(tuple(data[j, i[1]]) == blue):
            fallOnWater += 1
            fallCols.add(i[1])
            break
end = time()

print("O número de meteoros encontrados foi: ", meteors)
print("O número de estrelas encontradas foi: ", stars)
print("O número de meteoros que cairão na água é: ", fallOnWater)
print("Tempo de processamento: ", end - start)
