class Solution:
    EMPTY_TOKEN = "."

    def check_square(self, start_x, start_y, board) -> bool:
        seen = set()

        for x in range(start_x, start_x + 3):
            for y in range(start_y, start_y + 3):
                character = board[y][x]

                if character == self.EMPTY_TOKEN:
                    continue

                if character in seen:
                    return False

                seen.add(character)

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[row])):
                character = board[row][col]

                if character == self.EMPTY_TOKEN:
                    continue

                if character in seen:
                    return False

                seen.add(character)

        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                character = board[row][col]

                if character == self.EMPTY_TOKEN:
                    continue

                if character in seen:
                    return False
                    
                seen.add(character)

        coords = [
            (x, y) 
            for y in range(0, len(board), 3) 
            for x in range(0, len(board[0]), 3)
        ]

        for x, y in coords:
            if not self.check_square(x, y, board):
                return False

        return True
        
            
        