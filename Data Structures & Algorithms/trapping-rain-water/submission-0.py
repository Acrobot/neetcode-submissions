class Solution:
    def trap(self, height: List[int]) -> int:
        peaks_right = []

        max_peak = 0
        for h in height[::-1]:
            max_peak = max(max_peak, h)
            peaks_right.append(max_peak)

        max_peak = 0
        water = 0
        for idx, h in enumerate(height):
            max_peak = max(max_peak, h)
            right_peak = peaks_right[len(height)-idx-1]
            water += min(max_peak, right_peak) - h
            print(f"max: {max_peak}, right: {right_peak}, water: {water}")

        return water
        