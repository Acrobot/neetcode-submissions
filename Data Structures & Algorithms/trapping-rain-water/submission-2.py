class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1
        max_h_left = height[l]
        max_h_right = height[r]

        total_water = 0

        while l < r:
            if max_h_left < max_h_right:
                l += 1
                max_h_left = max(max_h_left, height[l])
                total_water += max_h_left - height[l]
            else:
                r -= 1
                max_h_right = max(max_h_right, height[r])
                total_water += max_h_right - height[r]
                

        return total_water
        