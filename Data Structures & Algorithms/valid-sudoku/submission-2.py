class Solution:
    BOARD_SIZE = 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0] * self.BOARD_SIZE
        rows = [0] * self.BOARD_SIZE
        boxes = [0] * self.BOARD_SIZE

        for row_idx, row in enumerate(board):
            for col_idx, val in enumerate(row):
                if val == '.':
                    continue

                num = int(val)
                    
                if cols[col_idx] & (1 << num):
                    return False
                else:
                    cols[col_idx] ^= (1 << num)
                
                if rows[row_idx] & (1 << num):
                    return False
                else:
                    rows[row_idx] ^= (1 << num)

                box_idx = (row_idx // 3) * 3 + col_idx // 3

                if boxes[box_idx] & (1 << num):
                    return False
                else:
                    boxes[box_idx] ^= (1 << num)

        return True
        