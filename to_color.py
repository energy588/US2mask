import cv2
import os
import numpy as np
import re
from skimage import io




def read_path(file_pathname):

    for filename in os.listdir(file_pathname):
        print(filename)
        img = cv2.imread(file_pathname + '/' + filename)

        rows = img.shape[0]
        cols = img.shape[1]
        for row in range(rows):
            for col in range(cols):
                if np.all(img[row, col] == 100):
                    img[row, col, 0] = 0
                    img[row, col, 1] = 128
                    img[row, col, 2] = 64
                elif np.all(img[row, col] == 200):
                    img[row, col, 0] = 0
                    img[row, col, 1] = 128
                    img[row, col, 2] = 192

        cv2.imwrite('/mask_color' + "/" + filename, img)

read_path("/mask")
