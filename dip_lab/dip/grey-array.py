from PIL import Image
from numpy import asarray

img = Image.open('vis.jpg')
numpydata = asarray(img)

print(numpydata)

