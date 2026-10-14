EMPTY = '.'
BOARD_SIZE = 9


class Solution:
    def isValidSeq(self, seq: List[str]) -> bool:
        nonempty = [d for d in seq if d != EMPTY]
        return len(set(nonempty)) == len(nonempty)

    isValidRow = isValidSeq

    def isValidCol(
        self,
        board: List[List[str]],
        col: int
    ) -> bool:
        seq = [row[col] for row in board]
        return self.isValidSeq(seq)


    def isValidSubbox(
        self, 
        board: List[List[str]], 
        start_x: int, 
        start_y: int
    ) -> bool:
        seq = board[start_y][start_x:start_x+3] + \
                board[start_y+1][start_x:start_x+3] + \
                board[start_y+2][start_x:start_x+3]

        return self.isValidSeq(seq)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(BOARD_SIZE):
            if not self.isValidRow(board[row]):
                return False

        for col in range(BOARD_SIZE):
            if not self.isValidCol(board, col):
                return False

        for sub_x in range(0, BOARD_SIZE, 3):
            for sub_y in range(0, BOARD_SIZE, 3):
                if not self.isValidSubbox(board, sub_x, sub_y):
                    return False

        return True
        