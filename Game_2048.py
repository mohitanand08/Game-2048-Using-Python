""" Game 2048 Using Python """
import random
# step - 1 : Starting the 2048 Game
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

# step - 2 : Adding new two to the matrix at empty space
def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while (mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2

# step - 3 : Current state of the game
def get_current_state(mat):
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "Congratulations !! You Won."
    # Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return "Game Not Over !!"
    # Every Row and column except last row and last column
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1] ):
                return "Game Not Over !!"
    # Last Row
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return "Game Not Over !!"
    # Last Column
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return "Game Not Over !!"

# step - 4 : Compress Function
def compress(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat
