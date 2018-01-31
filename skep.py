import numpy as np
import scipy.io
from PIL import Image
from scipy.ndimage.interpolation import zoom
import cv2
import os

height = 5
width = 5

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
Matrix = [[0 for x in range(width)] for y in range(height)]
Matrix = np.array(Matrix)
Matrix[0][0] = 21
Matrix[0][1] = 15
Matrix[0][2] = 14
Matrix[0][3] = 18
Matrix[0][4] = 22
Matrix[1][0] = 4
Matrix[1][1] = 2
Matrix[1][2] = 8
Matrix[1][3] = 13
Matrix[1][4] = 6
Matrix[2][0] = 9
Matrix[2][1] = 17
Matrix[2][2] = 24
Matrix[2][3] = 1
Matrix[2][4] = 7
Matrix[3][0] = 16
Matrix[3][1] = 3
Matrix[3][2] = 11
Matrix[3][3] = 25
Matrix[3][4] = 10
Matrix[4][0] = 5
Matrix[4][1] = 19
Matrix[4][2] = 23
Matrix[4][3] = 20
Matrix[4][4] = 12

arrangements = np.zeros((25, height, width))

#l = np.random.choice(a, (5, 5), False)
l = Matrix
initial_arrangement = l

for file in os.listdir("matFiles/"):
    count = 0

    filename = file  # "S001C001P001R001A002"

    for i in range(0, 25):

        mat = scipy.io.loadmat("matFiles/" + filename)  # 'matFiles/' + filename + '.skeleton.mat')

        framecount = mat["framecount"][0][0]

        # print(l)
        # print("Test ", mat['bodyinfo'][0][1]['bodies'][0][0]['joints'][0][0][0])

        for f in range(0, framecount):
            rgbArray = np.zeros((height, width, 3), 'uint8')
            for h in range(0, width):  # number of joints
                for w in range(0, height):
                    j = l[h][w] - 1
                    # print(j)
                    rgbArray[h, w, 0] = ((mat['bodyinfo'][0][f]['bodies'][0][0]['joints'][0][j][0][0][0] + 3.2160)/(2.0425 + 3.2160)) * 256
                    rgbArray[h, w, 1] = ((mat['bodyinfo'][0][f]['bodies'][0][0]['joints'][0][j][1][0][0] + 0.7359)/(1.4412 + 0.7359)) * 256
                    rgbArray[h, w, 2] = ((mat['bodyinfo'][0][f]['bodies'][0][0]['joints'][0][j][2][0][0] - 1.2587)/(4.8698 - 1.2587)) * 256
            img = Image.fromarray(rgbArray)
            # print(filename)
            img.save("intial_results" + "/" + str(f) + '.png')

        list_im = []
        for f in range(0, framecount):
            list_im.append("intial_results" + "/" + str(f) + '.png')

        imgs = [Image.open(i) for i in list_im]
        # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
        imgs_comb = np.hstack((np.asarray(i) for i in imgs))
        imgs_comb = Image.fromarray(imgs_comb)
        imgs_comb.save("intial_results" + "/" + 'temporalSeq' + str(count) + '.png')

        arrangements[i] = l
        l = np.roll(l, 1)
        count += 1
        print(i)

    initial_joints = arrangements[0]
    values = np.zeros(25)

    for arr in range(1, 25):
        for row in range(5):
            for col in range(5):
                k = np.where(arrangements[arr] == initial_joints[row][col])[0][0]
                m = np.where(arrangements[arr] == initial_joints[row][col])[1][0]
                values[arr] = values[arr] + max(abs(k - row), abs(m - col))

    print(values)

    values = sorted(range(len(values)), key=values.__getitem__)
    print(values)

    list_im = []
    for ar in range(0, 25):
        list_im.append("intial_results" + "/" + "temporalSeq" + str(ar) + '.png')

    imgs = [Image.open(i) for i in list_im]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    imgs_comb = np.vstack((np.asarray(i) for i in imgs))
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save("intial_results" + "/" + 'spatio-temporal-Seq.png')

    # resize image to 125 x 125
    resize_img = Image.open("intial_results" + "/" + 'spatio-temporal-Seq.png')
    resize_img = np.asarray(resize_img)
    print(resize_img.shape[1])
    small = cv2.resize(resize_img, (0, 0), fy=1, fx=125 / resize_img.shape[1])
    # resized_img = zoom(resize_img, [1,125/790])
    print(small.shape)
    # cv2.imwrite("resized_spatio_temporal.png", small)
    small = Image.fromarray(small)
    small.save("final_results/"+filename+".png")
    for f in os.listdir("intial_results"):
        os.remove("intial_results/" + f)
