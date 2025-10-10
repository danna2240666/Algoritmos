import matplotlib.pyplot as plt

plt.rcParams['image.cmap'] = 'gray'

import numpy as np
from skimage import io

image=io.imread("D:\Downloads\chuuya_ch.jpg", as_gray=False)
#imagen original
plt.imshow(image)
plt.figure()

#imagen para cada canal rojo, verde y azul como si fuera escala de blanco y negro
plt.imshow(image[:,:,0])
plt.title("Canal Rojo")
plt.figure()
plt.imshow(image[:,:,1])
plt.title("Canal Verde")
plt.figure()
plt.imshow(image[:,:,2])
plt.title("Canal Azul")
plt.figure()

#imagen en blanco y negro
img= io.imread("D:\Downloads\chuuya_ch.jpg", as_gray=True)
plt.imshow(img)
plt.figure()

#imagen recortada
cropped = image[30:(image.shape[0]-30)]
plt.imshow(cropped)
plt.figure()
cropped_xy= image[100:(image.shape[0]-100), 100:(image.shape[1]-100)]
plt.imshow(cropped_xy)

plt.show()