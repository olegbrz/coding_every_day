"""Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as
parameter. If the board is valid return 'Finished!', otherwise return
'Try again!'

Sudoku rules:

Complete the Sudoku puzzle so that each and every row, column, and region
contains the numbers one through nine only once.

Rows:

There are 9 rows in a traditional Sudoku puzzle. Every row must contain the
numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers
in any row. In other words, there can not be any rows that are identical.

In the illustration the numbers 5, 3, 1, and 2 are the "givens". They can not
be changed. The remaining numbers in black are the numbers that you fill in to
complete the row.

Columns:

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for
rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
Again, there may not be any duplicate numbers in any column. Each column will
be unique as a result.

In the illustration the numbers 7, 2, and 6 are the "givens". They can not be
changed. You fill in the remaining numbers as shown in black to complete the
column.

Regions:

A region is a 3x3 box like the one shown to the left. There are 9 regions in a
traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also
contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not
permitted in any region. Each region will differ from the other regions.

In the illustration the numbers 1, 2, and 8 are the "givens". They can not be
changed. Fill in the remaining numbers as shown in black to complete the
region.
"""

import numpy as np


def done_or_not(board):
    board = np.array(board)
    cols_ok = all([len(set(board[:, col])) == 9 for col in range(0, 9)])
    rows_ok = all([len(set(board[row, :])) == 9 for row in range(0, 9)])
    regs_ok = all([len(np.unique(board[row:row+3, col:col+3]))
                   == 9 for col in [0, 3, 6] for row in [0, 3, 6]])

    if cols_ok and rows_ok and regs_ok:
        return 'Finished!'
    else:
        return 'Try again!'
