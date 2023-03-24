import cv2 as cv
import numpy as np


def main():
    img_rgb = cv.imread('photo/tic3.jpg')
    img_rgb1 = cv.imread('photo/tic3.jpg')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    img_gray = cv.blur(img_gray, (7, 7))

    tempCrosss = cv.imread('./temp/crossPattern.jpg', cv.IMREAD_GRAYSCALE)
    tempCrosss = cv.blur(tempCrosss, (7, 7))

    tempCircle = cv.imread('./temp/circlePattern.jpg', cv.IMREAD_GRAYSCALE)
    # tempCircle = cv.blur(tempCircle, (7, 7))

    w, h = tempCrosss.shape[::-1]
    res = cv.matchTemplate(img_gray, tempCircle, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv.imwrite('res.png', img_rgb)

    res1 = cv.matchTemplate(img_gray, tempCrosss, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc1 = np.where(res1 >= threshold)
    for pt in zip(*loc1[::-1]):
        cv.rectangle(img_rgb1, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    cv.imwrite('res1.png', img_rgb1)


if __name__ == '__main__':
    main()
