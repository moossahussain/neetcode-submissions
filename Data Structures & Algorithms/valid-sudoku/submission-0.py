class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for column in range(9):
            seen = set()
            for i in  range(9):
                if board[i][column] == ".":
                    continue
                if board[i][column] in seen:
                    return False
                seen.add(board[i][column])

        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq//3) * 3 + i
                    col = (sq % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

