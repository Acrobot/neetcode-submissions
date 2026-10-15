class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False

        l = 0
        r = len(matrix)-1

        row = -1
        while l <= r:
            row = l + (r - l) // 2

            if matrix[row][0] >= target and matrix[row][-1] <= target:
                break
            elif matrix[row][0] > target:
                r = row - 1
            else:
                l = row + 1
        else:
            row = l + (r - l) // 2

        print(f"l: {l}, r: {r}, row: {row}")
        if matrix[row][0] > target or matrix[row][-1] < target:
            return False

        # We have the right now

        l = 0
        r = len(matrix[row])

        while l <= r:
            col = l + (r - l) // 2

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = col - 1
            else:
                l = col + 1

        return False