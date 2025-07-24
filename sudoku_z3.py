"""
The fucntions in this file solve the Sudoku problem using the z3 solver
"""
from z3 import *
import time

def z3_sat(mat):
    """
    Solve the sudoku problem by transforming it to sat problem
    :param mat: the sudoku matrix
    :return: the solved matrix
    """
    # Get the beginning time
    start = time.time()

    # Define the Boolean table
    tab = [[[Bool("tab_%s_%s_%s" % (i + 1, j + 1, k + 1)) for k in range(9)] for j in range(9)] for i in range(9)]

    # Define the solver
    s = Solver()

    # One cell take just one value
    for i in range(9):
        for j in range(9):
            for k in range(9):
                for t in range(9):
                    if (k != t):
                        s.add(Implies(tab[i][j][k], Not(tab[i][j][t])))

    # One number appear one time in one line
    for i in range(9):
        for k in range(9):
            s.add(Or(tab[i][0][k], tab[i][1][k], tab[i][2][k], tab[i][3][k], tab[i][4][k], tab[i][5][k], tab[i][6][k], tab[i][7][k], tab[i][8][k]))

    # One number appear one time in one row
    for j in range(9):
        for k in range(9):
            s.add(Or(tab[0][j][k], tab[1][j][k], tab[2][j][k], tab[3][j][k], tab[4][j][k], tab[5][j][k], tab[6][j][k], tab[7][j][k], tab[8][j][k]))

    # One number appear one time in each square
    for k in range(9):
        s.add(Or(tab[0][0][k], tab[0][1][k], tab[0][2][k], tab[1][0][k], tab[1][1][k], tab[1][2][k], tab[2][0][k], tab[2][1][k], tab[2][2][k]))
        s.add(Or(tab[3][0][k], tab[3][1][k], tab[3][2][k], tab[4][0][k], tab[4][1][k], tab[4][2][k], tab[5][0][k], tab[5][1][k], tab[5][2][k]))
        s.add(Or(tab[6][0][k], tab[6][1][k], tab[6][2][k], tab[7][0][k], tab[7][1][k], tab[7][2][k], tab[8][0][k], tab[8][1][k], tab[8][2][k]))
        s.add(Or(tab[0][3][k], tab[0][4][k], tab[0][5][k], tab[1][3][k], tab[1][4][k], tab[1][5][k], tab[2][3][k], tab[2][4][k], tab[2][5][k]))
        s.add(Or(tab[3][3][k], tab[3][4][k], tab[3][5][k], tab[4][3][k], tab[4][4][k], tab[4][5][k], tab[5][3][k], tab[5][4][k], tab[5][5][k]))
        s.add(Or(tab[6][3][k], tab[6][4][k], tab[6][5][k], tab[7][3][k], tab[7][4][k], tab[7][5][k], tab[8][3][k], tab[8][4][k], tab[8][5][k]))
        s.add(Or(tab[0][6][k], tab[0][7][k], tab[0][8][k], tab[1][6][k], tab[1][7][k], tab[1][8][k], tab[2][6][k], tab[2][7][k], tab[2][8][k]))
        s.add(Or(tab[3][6][k], tab[3][7][k], tab[3][8][k], tab[4][6][k], tab[4][7][k], tab[4][8][k], tab[5][6][k], tab[5][7][k], tab[5][8][k]))
        s.add(Or(tab[6][6][k], tab[6][7][k], tab[6][8][k], tab[7][6][k], tab[7][7][k], tab[7][8][k], tab[8][6][k], tab[8][7][k], tab[8][8][k]))

    # Add the already known cells
    for i in range(len(mat)):
        s.add(tab[mat[i][0] - 1][mat[i][1] - 1][mat[i][2] - 1])

    # Define the solution matrix
    sol = [[0 for j in range(9)] for i in range(9)]

    # Check if the SAT is satisfiable
    if s.check() == sat:
        m = s.model()
        # Get the result of the matrix
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    tmp = m.evaluate(tab[i][j][k])
                    if tmp:
                        sol[i][j] = k + 1

    # Get the end time
    end = time.time()
    # Print the time in seconds
    print(end - start)

    # Return the solution matrix
    # Return a 0 matrix if no solution
    return sol


def z3_int(mat):
    """
    Solve the sudoku problem by transforming it to sat problem
    :param mat: the sudoku matrix
    :return: the solved matrix
    """
    # Get the beginning time
    start = time.time()

    # Define the integer table
    tab = [[Int("x_%s_%s" % (i+1, j+1)) for j in range(9)] for i in range(9)]

    # Define the solver
    s = Solver()

    # All the numbers between 1 to 9
    for i in range(9):
        for j in range(9):
            s.add(And(1 <= tab[i][j], tab[i][j] <= 9))

    # One number one time in one line
    for i in range(9):
        s.add(Distinct(tab[i]))

    # One number one time in one row
    for j in range(9):
        s.add(Distinct([tab[i][j] for i in range(9)]))

    # One number appear one time in each square
    s.add(Distinct(tab[0][0], tab[0][1], tab[0][2], tab[1][0], tab[1][1], tab[1][2], tab[2][0], tab[2][1], tab[2][2]))
    s.add(Distinct(tab[3][0], tab[3][1], tab[3][2], tab[4][0], tab[4][1], tab[4][2], tab[5][0], tab[5][1], tab[5][2]))
    s.add(Distinct(tab[6][0], tab[6][1], tab[6][2], tab[7][0], tab[7][1], tab[7][2], tab[8][0], tab[8][1], tab[8][2]))
    s.add(Distinct(tab[0][3], tab[0][4], tab[0][5], tab[1][3], tab[1][4], tab[1][5], tab[2][3], tab[2][4], tab[2][5]))
    s.add(Distinct(tab[3][3], tab[3][4], tab[3][5], tab[4][3], tab[4][4], tab[4][5], tab[5][3], tab[5][4], tab[5][5]))
    s.add(Distinct(tab[6][3], tab[6][4], tab[6][5], tab[7][3], tab[7][4], tab[7][5], tab[8][3], tab[8][4], tab[8][5]))
    s.add(Distinct(tab[0][6], tab[0][7], tab[0][8], tab[1][6], tab[1][7], tab[1][8], tab[2][6], tab[2][7], tab[2][8]))
    s.add(Distinct(tab[3][6], tab[3][7], tab[3][8], tab[4][6], tab[4][7], tab[4][8], tab[5][6], tab[5][7], tab[5][8]))
    s.add(Distinct(tab[6][6], tab[6][7], tab[6][8], tab[7][6], tab[7][7], tab[7][8], tab[8][6], tab[8][7], tab[8][8]))

    # Add the already known cells
    for i in range(len(mat)):
        s.add(tab[mat[i][0] - 1][mat[i][1] - 1] == mat[i][2])

    # Define the solution matrix
    sol = [[0 for j in range(9)] for i in range(9)]

    # Check if the SAT is satisfiable
    if s.check() == sat:
        m = s.model()
        # Get the result of the matrix
        for i in range(9):
            for j in range(9):
                sol[i][j] = m.evaluate(tab[i][j])

    # Get the end time
    end = time.time()
    # Print the time in seconds
    print(end - start)

    # Return the solution matrix
    # Return a 0 matrix if no solution
    return sol

