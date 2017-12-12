from PIL import Image
import numpy as np

row = 2 
col = 2
rgbArray = np.zeros((row,col,3), 'uint8')

r = np.random.random((row,col))
rgbArray[..., 0] =r*256
rimg = Image.fromarray(r*256,'L')
rimg.save('rimg.jpeg')

g = np.random.random((row,col))
rgbArray[..., 1] =g*256
gimg = Image.fromarray(g*256,'L')
gimg.save('gimg.jpeg')

b = np.random.random((row,col))
rgbArray[..., 2] =b*256
bimg = Image.fromarray(b*256,'L')
bimg.save('bimg.jpeg')
print(rgbArray)
img = Image.fromarray(rgbArray)
img.save('myimg.jpeg')
