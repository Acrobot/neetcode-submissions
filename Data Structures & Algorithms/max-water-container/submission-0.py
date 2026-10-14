class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_idx, r_idx = 0, len(heights)-1
        top_volume = 0

        while l_idx < r_idx:
            l_height, r_height = heights[l_idx], heights[r_idx]

            volume = (r_idx - l_idx) * min(l_height, r_height)
            
            top_volume = max(volume, top_volume)

            if l_height < r_height:
                l_idx += 1
            else:
                r_idx -= 1

        return top_volume
        
        