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
