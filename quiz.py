def reverse_list(l: list):
    """
    Reverse a list without using any built-in functions.
    The function should return a reversed list.
    Input l is a list that may contain any type of data.
    """
    left, right = 0, len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return l

def solve_sudoku(matrix):
    """
    Write a program to solve a 9x9 Sudoku board.
    The board must be completed so that every row, column, and 3x3 section
    contains all digits from 1 to 9.
    Input: a 9x9 matrix representing the board.
    """
    
    n = 9
    def valid_num(i, j, num):
        for index in range(n):
            if matrix[i][index] == num or matrix[index][j] == num:
                return False
        
        row, col = i // 3 * 3, j // 3 * 3

        for row_index in range(row, row + 3):
            for col_index in range(col, col + 3):
                if matrix[row_index][col_index] == num:
                    return False
        return True
    
    def backtracking(matrix):

        for i in range(0, n):
            for j in range(0, n):
                if not matrix[i][j].isdigit():
                    for num in range(1, 10):
                        if valid_num(i, j, str(num)):
                            tmp = matrix[i][j]
                            matrix[i][j] = str(num)
                            if backtracking(matrix):
                                return True
                            matrix[i][j] = tmp
                    return False

        return True

    backtracking(matrix)


if __name__ == '__main__':
    pass