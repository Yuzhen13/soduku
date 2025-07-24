"""
Main file to launch the sudoku game
"""

from sudoku_z3 import *
from solver import *

def main():
    mat = [[1,1,2],
           #[1,3,2],
[1,2,9],
[1,4,3],
[1,6,8],
[2,3,6],
[2,4,4],
[2,8,5],
[3,4,7],
[3,8,9],
[4,3,1],
[4,9,8],
[5,1,7],
[5,5,9],
[5,7,3],
[6,1,3],
[6,9,5],
[7,6,2],
[7,9,6],
[8,2,8],
[8,5,1],
[8,7,5],
[9,1,5],
[9,2,2],
[9,5,8]]

    mat2 = [
        [1,1,1],[1,5,6],[1,7,9],
        [2,3,6],[2,4,3],
        [3,1,7],[3,2,2],[3,3,8],[3,6,9],[3,8,3],
        [4,8,2],
        [5,6,6],[5,9,4],
        [6,5,2],[6,6,4],[6,7,1],[6,9,9],
        [7,3,9],[7,4,1],[7,9,7],
        [8,1,5],[8,2,8],[8,6,3],
        [9,3,3],[9,4,2]
        ]

    sol = solver_back_tracking(mat, 0)
    if sol[0][0] == 0:
        print("No solution")
    else:
        for i in range(9):
            print(sol[i])


    sol = solver_back_tracking(mat, 1)
    if sol[0][0] == 0:
        print("No solution")
    else:
        for i in range(9):
            print(sol[i])


    sol = solver_back_tracking(mat, 2)
    if sol[0][0] == 0:
        print("No solution")
    else:
        for i in range(9):
            print(sol[i])

    sol = z3_sat(mat)

    sol = z3_int(mat)

    # Check if there is a solution
    if sol[0][0] == 0:
        print("No solution")
    else:
        for i in range(9):
            print(sol[i])

    sol = z3_sat(mat)

    sol = z3_int(mat)
    # Check if there is a solution
    if sol[0][0] == 0:
        print("No solution")
    else:
        for i in range(9):
            print(sol[i])
            




if __name__ == '__main__':
    main()




