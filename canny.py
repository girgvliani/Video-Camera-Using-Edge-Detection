import numpy as np
import cv2 as cv
from scipy import ndimage


def gaussianFil(img):
    return cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)


def grad(img):
    return cv.Laplacian(img, cv.CV_64F)


def hysteresis(img):
    highThreshold = 21
    lowThreshold = 15
    M, N, tup = img.shape
    Non_max = np.zeros((M, N), dtype=np.uint8)

    M, N = Non_max.shape
    out = np.zeros((M, N), dtype=np.uint8)

    strong_i, strong_j = np.where(Non_max >= highThreshold)
    zeros_i, zeros_j = np.where(Non_max < lowThreshold)

    weak_i, weak_j = np.where(
        (Non_max <= highThreshold) & (Non_max >= lowThreshold))

    out[strong_i, strong_j] = 255
    out[zeros_i, zeros_j] = 0
    out[weak_i, weak_j] = 75
    return out


def canny(img):
    blured = gaussianFil(img)  # 1 st step of canny detection
    intenseGrad = grad(blured)  # 2 nd and 3 rd parts of canny united
    ans = hysteresis(intenseGrad)
    return ans
