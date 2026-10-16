class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[l] < nums[mid]:
                # Left half sorted
                if nums[l] <= target <= nums[mid - 1]:
                    r = mid
                else:
                    l = mid + 1
            else:
                # Right half sorted
                if nums[mid] <= target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid

        return l if l < len(nums) and nums[l] == target else -1
