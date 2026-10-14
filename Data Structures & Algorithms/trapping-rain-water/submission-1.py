class Solution:
    def trap(self, height: List[int]) -> int:
        max_h_left = [0] * len(height)
        max_h_right = [0] * len(height)

        for idx, h in enumerate(height):
            if idx == 0:
                max_h_left[idx] = h
            else:
                max_h_left[idx] = max(max_h_left[idx-1], h)
            
        for idx, h in enumerate(height[::-1]):
            if idx == 0:
                max_h_right[len(height)-idx-1] = h
            else:
                max_h_right[len(height)-idx-1] = \
                    max(max_h_right[len(height)-idx], h)

        total_water = 0

        for idx, h in enumerate(height):
            total_water += max(
                min(max_h_left[idx], max_h_right[idx]) - h, 0
            )

        return total_water
        