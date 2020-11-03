def print_table(enter_cells):
    print("---------")
    print()
    print("| " + enter_cells[0][0] + " " + enter_cells[0][1] + " " + enter_cells[0][2] + " " + "|")
    print()
    print("| " + enter_cells[1][0] + " " + enter_cells[1][1] + " " + enter_cells[1][2] + " " + "|")
    print()
    print("| " + enter_cells[2][0] + " " + enter_cells[2][1] + " " + enter_cells[2][2] + " " + "|")
    print()
    print("---------")

def check_game_table(enter_cells):
    x_count = 0
    o_count = 0
    e_count = 0
    for i in enter_cells:
        for j in i:
            if j == "X":
                x_count += 1
            elif j == "O":
                o_count += 1
            else:
                e_count += 1
    l_first_second_or_third = (enter_cells[0] == "XXX" or enter_cells[0] == "OOO") and (
                (enter_cells[1] == "XXX" or enter_cells[1] == "OOO") or (
                    enter_cells[2] == "XXX" or enter_cells[2] == "OOO"))
    l_second_and_third = (enter_cells[2] == "XXX" or enter_cells[2] == "OOO") and (
                enter_cells[1] == "XXX" or enter_cells[1] == "OOO")
    the_first_column_x = enter_cells[0][0] == 'X' and enter_cells[1][0] == 'X' and enter_cells[2][0] == 'X'
    the_first_column_o = enter_cells[0][0] == 'O' and enter_cells[1][0] == 'O' and enter_cells[2][0] == 'O'
    the_second_column_x = enter_cells[0][1] == 'X' and enter_cells[1][1] == 'X' and enter_cells[2][1] == 'X'
    the_second_column_o = enter_cells[0][1] == 'O' and enter_cells[1][1] == 'O' and enter_cells[2][1] == 'O'
    the_third_column_x = enter_cells[0][2] == 'X' and enter_cells[1][2] == 'X' and enter_cells[2][2] == 'X'
    the_third_column_o = enter_cells[0][2] == 'O' and enter_cells[1][2] == 'O' and enter_cells[2][2] == 'O'
    upper_diagonal_x = enter_cells[0][0] == 'X' and enter_cells[1][1] == 'X' and enter_cells[2][2] == 'X'
    lower_diagonal_x = enter_cells[2][0] == 'X' and enter_cells[1][1] == 'X' and enter_cells[0][2] == 'X'
    upper_diagonal_o = enter_cells[0][0] == 'O' and enter_cells[1][1] == 'O' and enter_cells[2][2] == 'O'
    lower_diagonal_o = enter_cells[2][0] == 'O' and enter_cells[1][1] == 'O' and enter_cells[0][2] == 'O'

    if abs(x_count - o_count) >= 2:
        return "Impossible"
    elif l_first_second_or_third or l_second_and_third or ((the_first_column_o or the_first_column_x) and (
            (the_second_column_o or the_second_column_x) or (the_third_column_o or the_third_column_x))) or (
            (the_third_column_o or the_third_column_x) and (the_second_column_o or the_second_column_x)):
        return "Impossible"
    elif the_first_column_x or the_second_column_x or the_third_column_x or upper_diagonal_x or lower_diagonal_x or \
            enter_cells[0] == "XXX" or enter_cells[1] == "XXX" or enter_cells[2] == "XXX":
        return "X wins"
    elif the_first_column_o or the_second_column_o or the_third_column_o or upper_diagonal_o or lower_diagonal_o or \
            enter_cells[0] == "OOO" or enter_cells[1] == "OOO" or enter_cells[2] == "OOO":
        return "O wins"
    elif e_count == 0:
        return "Draw"
    else:
        return "Game not finished"

def update_game_table(x, y, value, table):
    work_list = list(table[x])
    work_list[y] = value
    table[x] = "".join(work_list)


def get_cell_address(x,y):
    if x == 1:
        if y == 1:
            return "2 0"
        elif y == 2:
            return "1 0"
        elif y == 3:
            return "0 0"
    elif x == 2:
        if y == 1:
            return "2 1"
        elif y == 2:
            return "1 1"
        elif y == 3:
            return "0 1"
    elif x == 3:
        if y == 1:
            return "2 2"
        elif y == 2:
            return "1 2"
        elif y == 3:
            return "0 2"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_cells = "_________"
    enter_cells = [start_cells[0:3], start_cells[3:6], start_cells[6:9]]
    print_table(enter_cells)
    value = 'X'
    while (True):
        if check_game_table(enter_cells) == "X wins":
            print ("X wins")
            break
        elif check_game_table(enter_cells) == "O wins":
            print ("O wins")
            break
        elif check_game_table(enter_cells) == "Draw":
            print ("Draw")
            break
        updated = False
        while(not updated):
            x, y = input("Enter the coordinates: ").split()
            if not(x.isdigit()) or not(y.isdigit()):
                print("You should enter numbers!")
                continue
            elif int(x) > 3 or int(y) > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            else:
                converted_x, converted_y = get_cell_address(int(x), int(y)).split()
                converted_x = int(converted_x)
                converted_y = int(converted_y)
                if not(enter_cells[converted_x][converted_y] == '_'):
                    print("This cell is occupied! Choose another one!")
                    continue
                else:
                    update_game_table(converted_x, converted_y, value, enter_cells)
                    updated = True
                    if value == 'X':
                        value = 'O'
                    else:
                        value = 'X'
                    print_table(enter_cells)
                    break