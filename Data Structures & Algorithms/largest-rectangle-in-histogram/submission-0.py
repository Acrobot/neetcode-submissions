class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for idx in range(len(heights)+1):
            while stack and (idx == len(heights) or heights[idx] < heights[stack[-1]]):
                rect_height = heights[stack.pop()]

                if not stack:
                    width = idx
                else:
                    width = idx - stack[-1] - 1
                
                max_area = max(max_area, rect_height * width)
            stack.append(idx)

        return max_area
                    