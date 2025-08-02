# Last updated: 8/2/2025, 4:54:14 PM
class Solution(object):
    def isValidBox(self, board, row, col):
        count = set()
        for r in range(row, row+3):
            for c in range(col, col+3):
                sqr = board[r][c]
                if sqr == ".":
                    continue
                else:
                    if sqr in count:
                        return False
                    else:
                        count.add(sqr)
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(len(board)):
            count = set()
            for col in range(len(board[0])):
                sqr = board[row][col]
                if sqr == ".":
                    continue
                else:
                    if sqr in count:
                        print("row")
                        return False
                    else:
                        count.add(sqr)
        
        for col in range(len(board[0])):
            count = set()
            for row in range(len(board)):
                sqr = board[row][col]
                if sqr == ".":
                    continue
                else:
                    if sqr in count:
                        print("col")
                        return False
                    else:
                        count.add(sqr)
        
        for row in range(0, len(board), 3):
            for col in range(0, len(board[0]), 3):
                if not self.isValidBox(board, row, col):
                    print("sq")
                    return False
        
        return True

        
        