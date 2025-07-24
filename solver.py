"""
Functions in this file solve the Sudoku problem using my own solvers
"""
import time

def solver_back_tracking(mat, strategie):
    """
    Solve the sudoku problem using the backtracking algorithm without learning
    :param mat: the sudoku matrix
    :param strategie: the strategie to use to solve the Sudoku
    :return: the solved matrix, a 0 matrix if no solution
    """
    # Get the beginning time
    start = time.time()

    # Define the result table
    tab = [[0 for j in range(9)] for i in range(9)]
    for i in range(len(mat)):
        tab[mat[i][0] - 1][mat[i][1] - 1] = mat[i][2]

    # Print the unsolved matrix
    """
    for i in range(9):
        print(tab[i])
    """

    # Check for the strategie
    if (strategie == 0):
        flag, tab = back_tracking_search(tab)
    elif (strategie == 1):
        flag, tab = back_tracking_search_opt1(0, 0, tab)
    elif (strategie == 2):
        # Initialize the unknown list
        unknown = []
        nb_possible = []
        counter = 0
        # Create the unknown list
        for i in range(9):
            for j in range(9):
                if (tab[i][j] == 0):
                    # Increasing the counter
                    counter += 1
                    # Record the index of this cell
                    unknown.append([i, j])
                    # Initialize the possibilities as 0
                    nb_possible.append(0)
                    is_possible = [True for j in range(10)]
                    for k in range(9):
                        # Mark the number in line as used
                        is_possible[tab[i][k]] = False
                        # Mark the number in row as used
                        is_possible[tab[k][j]] = False
                    # Find the locatio of the small 3 * 3
                    ti = i // 3
                    tj = j // 3
                    # Mark the number in the small 3 * 3 as used
                    for k in range(3):
                        for t in range(3):
                            is_possible[tab[ti * 3 + k][tj * 3 + t]] = False
                    # Count the possible cells
                    for k in range(1, 10):
                        if (is_possible[k]):
                            nb_possible[counter - 1] += 1
        # Sort the unknown list by an increasing number of possibilities by using bubble sort
        for i in range(0, counter - 1):
            for j in range(i + 1, counter):
                if (nb_possible[i] > nb_possible[j]):
                    tmp1 = unknown[i]
                    unknown[i] = unknown[j]
                    unknown[j] = tmp1
                    tmp2 = nb_possible[i]
                    nb_possible[i] = nb_possible[j]
                    nb_possible[j] = tmp2
        flag, tab = back_tracking_search_opt2(0, unknown, tab)

    # Get the end time
    end = time.time()
    # Print the time in seconds
    print(end - start)

    # Return the solution matrix
    # Return a 0 matrix if no solution
    if (flag):
        return tab
    else:
        return [[0 for j in range(9)] for i in range(9)]




def back_tracking_search(tab):
    """
    Use the back tracking algorithm to find the possible solution for a matrix
    :param tab: the given matrix
    :return: the feasible solution and an indicator if there is a possible solution
    """
    # Find the first unkown cell
    flag = False
    for i in range(9):
        for j in range(9):
            if (tab[i][j] == 0):
                flag = True
                break
        if flag:
            break

    # Check if goes to the end of the algorithm
    if (not flag):
        return True, tab

    # Find the possible number
    is_possible = [True for j in range(10)]
    for k in range(9):
        # Mark the number in line as used
        is_possible[tab[i][k]] = False
        # Mark the number in row as used
        is_possible[tab[k][j]] = False
    # Find the locatio of the small 3 * 3
    ti = i // 3
    tj = j // 3
    # Mark the number in the small 3 * 3 as used
    for k in range(3):
        for t in range(3):
            is_possible[tab[ti * 3 + k][tj * 3 + t]] = False

    # Use back tracking algorithm to find the number
    for k in range(1, 10):
        if (is_possible[k]):
            # Set the value
            tab[i][j] = k
            # Go for the next number
            found, tab = back_tracking_search(tab)
            # End if finish filling the matrix
            if (found):
                return True, tab
            # Set back the value as 0
            tab[i][j] = 0

    # back_tracking_search(tab)
    return(False, tab)




def back_tracking_search_opt1(si, sj, tab):
    """
    Give a small optimization for the previous algorithm
    Each time when we want to find the first unkown one
    Store the position of the previous cell we searched
    :param si: the line of previous cell
    :param sj: the row of previous cell
    :param tab: the matrix
    :return: the feasible solution and an indicator if there is a possible solution
    """
    # Find the first unkown cell
    flag = False
    i = si
    j = sj
    for j in range(j, 9):
        if (tab[si][j] == 0):
            flag = True
            break

    if (not flag):
        for i in range(i, 9):
            for j in range(0, 9):
                if (tab[i][j] == 0):
                    flag = True
                    break
            if flag:
                break

    # Check if goes to the end of the algorithm
    if (not flag):
        return True, tab

    # Find the possible number
    is_possible = [True for j in range(10)]
    for k in range(9):
        # Mark the number in line as used
        is_possible[tab[i][k]] = False
        # Mark the number in row as used
        is_possible[tab[k][j]] = False
    # Find the locatio of the small 3 * 3
    ti = i // 3
    tj = j // 3
    # Mark the number in the small 3 * 3 as used
    for k in range(3):
        for t in range(3):
            is_possible[tab[ti * 3 + k][tj * 3 + t]] = False

    # Use back tracking algorithm to find the number
    for k in range(1, 10):
        if (is_possible[k]):
            # Set the value
            tab[i][j] = k
            # Go for the next number
            found, tab = back_tracking_search_opt1(i, j, tab)
            # End if finish filling the matrix
            if (found):
                return True, tab
            # Set back the value as 0
            tab[i][j] = 0

    # back_tracking_search(tab)
    return(False, tab)




def back_tracking_search_opt2(index, unknown, tab):
    """
    Give another optimization for the previous algorithm
    Search from the cell who has less possibilities
    :param index: an indicator of the unknown cells
    :param unknown: all the unknown cells with an increasing order of the possibilities
    :param tab: the matrix
    :return: the feasible solution and an indicator if there is a possible solution
    """
    # Check if goes to the end of the algorithm
    if (index == len(unknown)):
        return True, tab

    # Find the possible number
    is_possible = [True for j in range(10)]
    for k in range(9):
        # Mark the number in line as used
        is_possible[tab[unknown[index][0]][k]] = False
        # Mark the number in row as used
        is_possible[tab[k][unknown[index][1]]] = False
    # Find the locatio of the small 3 * 3
    ti = unknown[index][0] // 3
    tj = unknown[index][1] // 3
    # Mark the number in the small 3 * 3 as used
    for k in range(3):
        for t in range(3):
            is_possible[tab[ti * 3 + k][tj * 3 + t]] = False

    # Use back tracking algorithm to find the number
    for k in range(1, 10):
        if (is_possible[k]):
            # Set the value
            tab[unknown[index][0]][unknown[index][1]] = k
            # Go for the next number
            found, tab = back_tracking_search_opt2(index + 1, unknown, tab)
            # End if finish filling the matrix
            if (found):
                return True, tab
            # Set back the value as 0
            tab[unknown[index][0]][unknown[index][1]] = 0

    # back_tracking_search(tab)
    return(False, tab)

