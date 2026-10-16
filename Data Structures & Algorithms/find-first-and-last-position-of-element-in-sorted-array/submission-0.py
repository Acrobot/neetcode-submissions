class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if l >= len(nums) or nums[l] != target:
            return [-1, -1]

        start = l

        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return [start, l - 1]
