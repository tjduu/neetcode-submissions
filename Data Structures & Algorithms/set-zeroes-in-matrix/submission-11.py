import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows = [False]*ROWS
        cols = [False]*COLS
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(ROWS):
            for j in range(COLS):
                if rows[i] == True or cols[j] ==True:
                    matrix[i][j] = 0




