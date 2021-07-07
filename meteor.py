from PIL import Image
import numpy as np

img = Image.open('image-151.png')
data = np.asarray(img)

arr1 = [0, 1, 2, 3]
arr2 = [0, 1, 2, 3]
print(arr1 == arr2)

cores = []
for i in data:
    for j in i:
        if(any(j not in cores)):
            cores.append(j)

print(cores)
