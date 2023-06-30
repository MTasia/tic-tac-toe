import cv2

from src.find_play_field import preparate_image, find_sheet, image_cropping, find_figure
from utils.const import X, O


def determ_figures(img):
    img0 = img
    thresh = preparate_image(img)

    # find the borders of a sheet of paper
    sheet_contours = find_sheet(thresh, img)

    # cut along the edges of the sheet of paper
    crop_img, img0 = image_cropping(img0, thresh, sheet_contours)

    tempCircle = cv2.imread('temp/circleCaseTemp.png', cv2.IMREAD_GRAYSCALE)
    tempCrosss = cv2.imread('temp/crossCaseTemp.png', cv2.IMREAD_GRAYSCALE)
    circle, cross = find_figure(crop_img, img0, tempCircle, tempCrosss)

    return O, X

