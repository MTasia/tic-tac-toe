import cv2

from utils.const import *


def create_temp(crop_img, img0, field_contours):
    (y0, x0), (y3, x3) = field_contours
    field_w, field_h = x3 - x0, y3 - y0
    y1, x1, = int(y0 + 1 / 3 * field_h), int(x0 + 1 / 3 * field_w)
    y2, x2, = int(y0 + 2 / 3 * field_h), int(x0 + 2 / 3 * field_w)
    e = 15

    # cross
    cell_cross = crop_img[x2 + e:x3 - e, y0 + e:y1 - e]
    cell_cross0 = img0[x2 + e:x3 - e, y0 + e:y1 - e]

    # circle
    cell_circle = crop_img[x2 + e:x3 - e, y2 + e:y3 - e]
    cell_circle0 = img0[x2 + e:x3 - e, y2 + e:y3 - e]

    cv2.imwrite('temp/crossTemp.jpg', cell_cross)
    cv2.imwrite('temp/circleTemp.jpg', cell_circle)

    cv2.imshow('cell for temp circle', cell_circle)
    cv2.waitKey(0)
    cv2.imshow('cell for temp cross', cell_cross)
    cv2.waitKey(0)


def print_m(field):
    for f in field:
        print(*f)
    print()


def print_field(field):
    for line in field:
        for cell in line:
            print(cell, end=' | ')
        print()
        print('___________')
    print()


def cell_is_free(cell):
    return cell != X and cell != O
