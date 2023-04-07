import os

import cv2
import numpy as np

from utils.const import X, O
from utils.helps import print_m

os.chdir('/Users/taya/PycharmProjects/tic-tac-toe/')


def find_line(crop_img, img0, color):
    # Apply edge detection method on the image
    edges = cv2.Canny(crop_img, 50, 150, apertureSize=3)

    # This returns an array of r and theta values
    lines = cv2.HoughLinesP(
        edges,  # Input edge image
        1,  # Distance resolution in pixels
        np.pi / 180,  # Angle resolution in radians
        threshold=100,  # Min number of votes for valid line
        minLineLength=5,  # Min allowed length of line
        maxLineGap=10  # Max allowed gap between line for joining them
    )

    # Iterate over points
    lines_list = []
    if lines is None:
        return []
    for points in lines:
        # Extracted points nested in the list
        x1, y1, x2, y2 = points[0]
        # Draw the lines joing the points
        # On the original image
        cv2.line(img0, (x1, y1), (x2, y2), color, 2)

        # Maintain a simples lookup list for points
        lines_list.append([(x1, y1), (x2, y2)])

    cv2.imshow('lines Image', img0)
    cv2.waitKey(0)

    return lines_list


def preparate_image(img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(imgray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    cv2.imshow('Binary Image', thresh)
    # cv2.waitKey(0)

    # thresh = cv2.blur(thresh, (7, 7))

    return thresh


def find_contours(thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # убираем лишние контуры
    new_cont = []
    for c in contours:
        # print(len(c))
        if len(c) > 100:
            new_cont.append(c)
    return new_cont


def find_sheet(thresh, img):
    # находим контуры и убираем лишние
    new_cont = find_contours(thresh)

    # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    w, h = img.shape[:2]
    x_min, y_min = h, w
    x_max, y_max = 0, 0
    for c in new_cont:
        for p in c:
            # print(p)
            if p[0][0] < y_min:
                y_min = p[0][0]
            if p[0][1] < x_min:
                x_min = p[0][1]
            if p[0][0] > y_max:
                y_max = p[0][0]
            if p[0][1] > x_max:
                x_max = p[0][1]

    return [(y_min, x_min), (y_max, x_max)]


def image_cropping(img, img0, thresh, contours):
    (y_min, x_min), (y_max, x_max) = contours

    cv2.circle(img, (y_min, x_min), 6, (0, 0, 255), 3)
    cv2.circle(img, (y_max, x_max), 6, (0, 0, 255), 3)
    # cv2.imshow('cont Image', img)
    # cv2.waitKey(0)

    e = 30
    img0 = img0[x_min + e:x_max - e, y_min + e:y_max - e]  # не понимаю, почему сначала x а потом y
    crop_img = thresh[x_min + e:x_max - e, y_min + e:y_max - e]
    # cv2.imshow('resize by sheet image', crop_img)
    # cv2.waitKey(0)

    return crop_img, img0


def find_field(crop_img, img0):
    color = (0, 255, 0)
    lines_list = find_line(crop_img, img0, color)
    w, h = img0.shape[:2]

    new_line = []
    line_x_min, line_y_min = h, w
    line_x_max, line_y_max = 0, 0
    for line in lines_list:
        # line = line[0]
        y_start, x_start = line[0][0], line[0][1]
        y_end, x_end = line[1][0], line[1][1]
        if y_start < line_y_min:
            line_y_min = y_start
        if x_start < line_x_min:
            line_x_min = x_start
        if y_end > line_y_max:
            line_y_max = y_end
        if x_end > line_x_max:
            line_x_max = x_end

    cv2.circle(img0, (line_y_min, line_x_min), 6, (0, 0, 255), 3)
    cv2.circle(img0, (line_y_max, line_x_max), 6, (0, 0, 255), 3)

    cv2.line(img0, (line_y_min, line_x_min), (line_y_min, line_x_max), (0, 0, 255), 2)
    cv2.line(img0, (line_y_min, line_x_min), (line_y_max, line_x_min), (0, 0, 255), 2)
    cv2.line(img0, (line_y_max, line_x_min), (line_y_max, line_x_max), (0, 0, 255), 2)
    cv2.line(img0, (line_y_min, line_x_max), (line_y_max, line_x_max), (0, 0, 255), 2)

    cv2.line(img0, (line_y_min + int(1 / 3 * (line_y_max - line_y_min)), line_x_min),
             (line_y_min + int(1 / 3 * (line_y_max - line_y_min)), line_x_max), (0, 0, 255), 2)
    cv2.line(img0, (line_y_min + int(2 / 3 * (line_y_max - line_y_min)), line_x_min),
             (line_y_min + int(2 / 3 * (line_y_max - line_y_min)), line_x_max), (0, 0, 255), 2)
    cv2.line(img0, (line_y_min, line_x_min + int(1 / 3 * (line_x_max - line_x_min))),
             (line_y_max, line_x_min + int(1 / 3 * (line_x_max - line_x_min))), (0, 0, 255), 2)
    cv2.line(img0, (line_y_min, line_x_min + int(2 / 3 * (line_x_max - line_x_min))),
             (line_y_max, line_x_min + int(2 / 3 * (line_x_max - line_x_min))), (0, 0, 255), 2)

    cv2.imshow('cont-fiedld Image', img0)
    cv2.waitKey(0)

    return [(line_y_min, line_x_min), (line_y_max, line_x_max)]


def find_figure(img, img0):
    tempCrosss = cv2.imread('./temp/crossPattern.jpg', cv2.IMREAD_GRAYSCALE)
    tempCircle = cv2.imread('./temp/circlePattern.jpg', cv2.IMREAD_GRAYSCALE)

    w, h = tempCrosss.shape[:2]
    res = cv2.matchTemplate(img, tempCircle, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    circle = []
    for pt in zip(*loc[::-1]):
        circle.append([pt, (pt[0] + w, pt[1] + h)])
        cv2.rectangle(img0, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)

    res1 = cv2.matchTemplate(img, tempCrosss, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc1 = np.where(res1 >= threshold)
    cross = []
    for pt in zip(*loc1[::-1]):
        cross.append([pt, (pt[0] + w, pt[1] + h)])
        cv2.rectangle(img0, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

    cv2.imshow('cross', img0)
    cv2.waitKey(0)

    return circle, cross


def find_tic_tac_toe(crop_img, field_contours, img0):
    (y0, x0), (y3, x3) = field_contours
    field_w, field_h = x3 - x0, y3 - y0
    y1, x1, = int(y0 + 1 / 3 * field_h), int(x0 + 1 / 3 * field_w)
    y2, x2, = int(y0 + 2 / 3 * field_h), int(x0 + 2 / 3 * field_w)
    field_point = [[y0, y1, y2, y3], [x0, x1, x2, x3]]
    circle, cross = find_figure(crop_img, img0)

    n = 3
    field = [['-' for j in range(n)] for j in range(n)]

    # circle
    for i in range(len(circle)):
        yu, xu = circle[i][0]
        yd, xd = circle[i][1]
        xc = int((xu + xd) / 2)
        yc = int((yu + yd) / 2)

        # cv2.circle(img0, (yc, xc), 6, (0, 0, 255), 3)
        # cv2.circle(img0, (y0, x0), 6, (0, 0, 255), 3)
        # cv2.circle(img0, (y1, x1), 6, (0, 0, 255), 3)

        # 00 - 02
        if y0 < yc < y1 and x0 < xc < x1:
            field[0][0] = O
        elif y0 < yc < y1 and x1 < xc < x2:
            field[1][0] = O
        elif y0 < yc < y1 and x2 < xc < x3:
            field[2][0] = O
        # 10 - 12
        elif y1 < yc < y2 and x0 < xc < x1:
            field[0][1] = O
        elif y1 < yc < y2 and x1 < xc < x2:
            field[1][1] = O
        elif y1 < yc < y2 and x2 < xc < x3:
            field[2][1] = O
        # 20 - 22
        elif y2 < yc < y3 and x0 < xc < x1:
            field[0][2] = O
        elif y2 < yc < y3 and x1 < xc < x2:
            field[1][2] = O
        elif y2 < yc < y3 and x2 < xc < x3:
            field[2][2] = O

    # cross
    for i in range(len(cross)):
        yu, xu = cross[i][0]
        yd, xd = cross[i][1]
        xc = int((xu + xd) / 2)
        yc = int((yu + yd) / 2)

        # cv2.circle(img0, (yc, xc), 6, (0, 0, 255), 3)
        # cv2.circle(img0, (y0, x0), 6, (0, 0, 255), 3)
        # cv2.circle(img0, (y1, x1), 6, (0, 0, 255), 3)

        # 00 - 02
        if y0 < yc < y1 and x0 < xc < x1:
            field[0][0] = X
        elif y0 < yc < y1 and x1 < xc < x2:
            field[1][0] = X
        elif y0 < yc < y1 and x2 < xc < x3:
            field[2][0] = X
        # 10 - 12
        elif y1 < yc < y2 and x0 < xc < x1:
            field[0][1] = X
        elif y1 < yc < y2 and x1 < xc < x2:
            field[1][1] = X
        elif y1 < yc < y2 and x2 < xc < x3:
            field[2][1] = X
        # 20 - 22
        elif y2 < yc < y3 and x0 < xc < x1:
            field[0][2] = X
        elif y2 < yc < y3 and x1 < xc < x2:
            field[1][2] = X
        elif y2 < yc < y3 and x2 < xc < x3:
            field[2][2] = X
    print("first field")
    print_m(field)

    return field


def find_play_field(img):
    img0 = img

    thresh = preparate_image(img)
    cv2.imshow('Blur Image', thresh)
    cv2.waitKey(0)

    # find the borders of a sheet of paper
    sheet_contours = find_sheet(thresh, img)

    # cut along the edges of the sheet of paper
    crop_img, img0 = image_cropping(img, img0, thresh, sheet_contours)

    # find the boundaries of the playing field
    field_contours = find_field(crop_img, img0)

    # find tic-tac-toe on the field
    tic_tac_toe = find_tic_tac_toe(crop_img, field_contours, img0)

    return tic_tac_toe
