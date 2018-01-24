import scipy.io
from PIL import Image
import numpy as np

height = 5
width = 5
rgbArray = np.zeros((height,width,3),'uint8')

mat = scipy.io.loadmat('bodyinfo.mat')

framecount = mat['framecount'][0][0]
print(framecount)

for f in range(0,framecount):
j = 0
for h in range(0,height): #number of joints
    for w in range(0,width):
        rgbArray[h,w, 0]  = mat['bodyinfo'][0][0][11][0][j][0][0][0]*256
        rgbArray[h,w, 1]  = mat['bodyinfo'][0][0][11][0][j][1][0][0]*256
        rgbArray[h,w, 2]  = mat['bodyinfo'][0][0][11][0][j][2][0][0]*256
        j+=1

img = Image.fromarray(rgbArray[..., 0])
img.save('x.png')

img = Image.fromarray(rgbArray[..., 1])
img.save('y.png')

img = Image.fromarray(rgbArray[..., 2])
img.save('z.png')

#print(rgbArray)
img = Image.fromarray(rgbArray)
img.save('myimg.png')
#print(np.array(img))
        
