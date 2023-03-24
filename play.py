def check_win(field):
    if field[0][0] == field[0][1] and field[0][1] == field[0][2]:
        return True, field[0][0]
    elif field[1][0] == field[1][1] and field[1][1] == field[1][2]:
        return True, field[1][0]
    elif field[2][0] == field[2][1] and field[2][1] == field[2][2]:
        return True, field[2][0]

    elif field[0][0] == field[1][0] and field[1][0] == field[2][0]:
        return True, field[0][0]
    elif field[0][1] == field[1][1] and field[1][1] == field[2][1]:
        return True, field[0][1]
    elif field[0][2] == field[1][2] and field[1][2] == field[2][2]:
        return True, field[0][0]

    elif field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        return True, field[0][0]
    elif field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        return True, field[0][2]

    return False, 0


def make_move(field, robot):
    if robot == 1:
        player = 2
    else:
        player = 1



    for i in range(len(field)):
        if field[i][0] == player and field[i][1] == player:
            field[i][2] = robot
            return field
        if field[i][1] == player and field[i][2] == player:
            field[i][0] = robot
            return field
        if field[i][0] == player and field[i][2] == player:
            field[i][1] = robot
            return field

        if field[0][i] == player and field[1][i] == player:
            field[2][i] = robot
            return field
        if field[1][i] == player and field[2][i] == player:
            field[0][i] = robot
            return field
        if field[0][i] == player and field[2][i] == player:
            field[1][i] = robot
            return field

    if field[0][0] == player and field[1][1] == player:
        field[2][2] = robot
        return field
    if field[2][2] == player and field[1][1] == player:
        field[0][0] = robot
        return field
    if field[0][0] == player and field[2][2] == player:
        field[1][1] = robot
        return field

    if field[2][0] == player and field[1][1] == player:
        field[0][2] = robot
        return field
    if field[0][2] == player and field[1][1] == player:
        field[2][0] = robot
        return field
    if field[2][0] == player and field[0][2] == player:
        field[1][1] = robot
        return field

    return field


def play(field, robot):
    n = 3
    is_win, winner = check_win(field)
    if is_win:
        if robot == winner:
            return field, "robot win"
        else:
            return field, "you are win"

    new_field = make_move(field, robot)

    return new_field, "game continues"
