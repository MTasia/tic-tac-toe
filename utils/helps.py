from utils.const import *


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
