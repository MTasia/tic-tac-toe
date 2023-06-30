import cv2

from utils.const import *


# get templates from current field
# this func call only once, for creating new templates
def create_temp(crop_img, img0, field_contours):
    (y0, x0), (y3, x3) = field_contours
    field_w, field_h = x3 - x0, y3 - y0
    y1, x1, = int(y0 + 1 / 3 * field_h), int(x0 + 1 / 3 * field_w)
    y2, x2, = int(y0 + 2 / 3 * field_h), int(x0 + 2 / 3 * field_w)
    e = 15

    # cross
    y0_cross = y1
    y1_cross = y2
    x0_cross = x1
    x1_cross = x2
    cell_cross = crop_img[x0_cross + e:x1_cross - e, y0_cross + e:y1_cross - e]
    cell_cross0 = img0[x0_cross + e:x1_cross - e, y0_cross + e:y1_cross - e]

    # circle
    y0_circle = y0
    y1_circle = y1
    x0_circle = x0
    x1_circle = x1
    cell_circle = crop_img[x0_circle + e:x1_circle - e, y0_circle + e:y1_circle - e]
    cell_circle0 = img0[x0_circle + e:x1_circle - e, y0_circle + e:y1_circle - e]

    cv2.imwrite('temp/emptyPlay.jpg', cell_cross)
    cv2.imwrite('temp/circleTemp.jpg', cell_circle)

    # cell_empty = img0[x0 + e:x1 - e, y0 + e:y1 - e]
    # cv2.imwrite('temp/circleTemp.jpg', cell_empty)

    cv2.imshow('cell for temp circle', cell_circle)
    cv2.waitKey(0)
    cv2.imshow('cell for temp cross', cell_cross)
    cv2.waitKey(0)


def matcing_filds(field, detect_field):
    for i in range(N):
        for j in range(N):
            if detect_field[i][j] == X or detect_field[i][j] == O:
                field[i][j] = detect_field[i][j]

    return field


def find_cell(new_field, field):
    for i in range(N):
        for j in range(N):
            if field[i][j] != new_field[i][j]:
                return i, j

    return -1, -1


def field_for_user(field):
    field_user = [['-' for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if field[i][j] == X or field[i][j] == O:
                field_user[i][j] = field[i][j]

    return field_user


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
