from pylab import *
from sklearn import datasets
faces = datasets.fetch_olivetti_faces()
faces.keys()
for i in range(10):
    face = faces.images[i]
    subplot(1, 10, i + 1)
    imshow(face.reshape((64, 64)), cmap='gray')
    axis('off')

