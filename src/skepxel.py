import scipy.io
from PIL import Image
import numpy as np

height = 5
width = 5
rgbArray = np.zeros((height,width,3),'uint8')

mat = scipy.io.loadmat('bodyinfo.mat')

j = 0
for h in range(0,height): #number of joints
    for w in range(0,width):
        rgbArray[h,w, 0]  = mat['body'][0][0][11][0][j][0][0][0]*256
        rgbArray[h,w, 1]  = mat['body'][0][0][11][0][j][1][0][0]*256
        rgbArray[h,w, 2]  = mat['body'][0][0][11][0][j][2][0][0]*256
        j+=1

img = Image.fromarray(rgbArray[..., 0])
img.save('x.jpeg')

img = Image.fromarray(rgbArray[..., 1])
img.save('y.jpeg')

img = Image.fromarray(rgbArray[..., 2])
img.save('z.jpeg')

print(rgbArray)
img = Image.fromarray(rgbArray)
img.save('myimg.jpeg')
        

