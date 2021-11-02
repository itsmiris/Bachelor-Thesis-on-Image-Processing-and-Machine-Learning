import cv2
import numpy as np
from numpy.typing import *


def color_descriptor(img: NDArray) -> NDArray:
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    levels = 8
    hhist = cv2.calcHist([hsv_image], [0], None, [levels], [0, 180])
    sumhhist = np.sum(hhist)
    hhist[:] = [x / sumhhist for x in hhist]
    shist = cv2.calcHist([hsv_image], [1], None, [levels], [0, 255])
    sumshist = np.sum(shist)
    shist[:] = [x / sumshist for x in shist]
    vhist = cv2.calcHist([hsv_image], [2], None, [levels], [0, 255])
    sumvhist = np.sum(vhist)
    vhist[:] = [x / sumvhist for x in vhist]
    colordescriptor = np.concatenate([hhist, shist, vhist]).flatten()
    return colordescriptor


def contrast_descriptor(img: NDArray) -> float:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    layer = img.copy()
    gp = [layer]
    for i in range(6):
        layer = cv2.pyrDown(layer)
        gp.append(layer)
    layer = gp[5]
    lap_pyr = [layer]
    for i in range(5, 0, -1):
        size = (gp[i - 1].shape[1], gp[i - 1].shape[0])
        gaussian_extend = cv2.pyrUp(gp[i], dstsize=size)
        laplacian = cv2.subtract(gp[i - 1], gaussian_extend)
        lap_pyr.append(laplacian)

    m, n = laplacian.shape
    descriptor_contrast = 0
    for i in range(m):
        for j in range(n):
            descriptor_contrast = descriptor_contrast + int(laplacian[i][j]) * int(laplacian[i][j])
    return descriptor_contrast / (m * n)
