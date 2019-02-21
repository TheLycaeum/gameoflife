import time
def get_live_neighbours(matrix,pos):
    m = matrix_order = len(matrix) - 1
    x,y = pos
    if x == 0 and y == 0: #top left corner
        return [matrix[0][1],matrix[1][0],matrix[1][1]].count(True)
    elif x == matrix_order and y == 0: #bottom left corner
        return [matrix[m-1][0],matrix[m-1][1],matrix[m][1]].count(True)
    elif x == 0 and y == matrix_order: #top right corner
        return [matrix[0][m-1],matrix[1][m-1],matrix[1][m]].count(True)
    elif x == matrix_order and y == matrix_order: #bottom right corner
        return [matrix[m-1][m-1],matrix[m-1][m],matrix[m][m-1]].count(True)
    elif x == 0: #first row
        return [matrix[0][y-1],matrix[0][y+1],matrix[1][y-1],matrix[1][y],matrix[1][y+1]].count(True)
    elif y == 0: #first column
        return [matrix[x-1][0],matrix[x+1][0],matrix[x-1][1],matrix[x][1],matrix[x+1][1]].count(True)
    elif x == matrix_order: # last row
        return [matrix[m-1][y-1],matrix[m-1][y],matrix[m-1][y+1],matrix[m][y-1],matrix[m][y+1]].count(True)
    elif y == matrix_order: # last column
        return [matrix[x-1][m-1],matrix[x-1][m],matrix[x][m-1],matrix[x+1][m-1],matrix[x+1][m]].count(True)
    else:
        return [matrix[x-1][y-1],matrix[x-1][y],matrix[x-1][y+1],matrix[x][y-1],
                matrix[x][y+1],matrix[x+1][y-1],matrix[x+1][y],matrix[x+1][y+1]].count(True)


def is_alive(matrix,position):
    live_cells = get_live_neighbours(matrix,position)
    x,y = position
    if matrix[x][y] == True and live_cells in (2,3):
        return True
    elif matrix[x][y] == False and live_cells == 3:
        return True
    else:
        return False


def update_state(matrix):
    order  = len(matrix)
    new_state = dead_matrix(len(matrix))

    for i in range(order):
        for j in range(order):
            if is_alive(matrix,[i,j]):
                new_state[i][j] = True
    return new_state


def dead_matrix(order):
    return [[False for _ in range(order)] for _ in range(order) ]


def init_state():
    # get matrix from user via file
    matrix = [[False,True,False,False,False],
              [False,True,False,False,False],
              [False,True,False,False,False],
              [False,False,False,False,False],
              [False,False,False,False,True]]
    return matrix

def print_matrix_diag(matrix):
    text = ""
    order = len(matrix)
    for i in range(order):
        for j in range(order):
            if matrix[i][j] == False:
                text = text + "- "
            else:
                text = text + "+ "
        text = text + "\n"
    return text

def simulation():
    matrix = init_state()
    print("initial state")
    print(print_matrix_diag(matrix))
    while True:
        next_state = update_state(matrix)
        diag = print_matrix_diag(next_state)
        print(diag)
        print("\n\n\n")
        matrix = next_state
        time.sleep(5)

if __name__ == "__main__":
    simulation()
