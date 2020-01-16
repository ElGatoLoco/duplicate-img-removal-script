import cv2
import numpy as np
import os

PATH = './path/to/images/folder'
DIFFERENCE_SUM_BOUNDARY = 100000

if __name__ == '__main__':
    (_, _, filenames) = next(os.walk(PATH))
    filenames.sort()
    a, b = 0, 1

    while b < len(filenames):
        img_a = '{}/{}'.format(PATH, filenames[a])
        img_b = '{}/{}'.format(PATH, filenames[b])
        difference = cv2.subtract(cv2.imread(img_a), cv2.imread(img_b))
        significant_difference = np.sum(difference) > DIFFERENCE_SUM_BOUNDARY
        if significant_difference:
            a = b
        else:
            os.remove(img_b)
        b += 1
