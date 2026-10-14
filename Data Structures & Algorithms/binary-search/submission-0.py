class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx, r_idx = 0, len(nums)-1

        while l_idx <= r_idx:
            mid = (r_idx + l_idx) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l_idx = mid + 1
            else:
                r_idx = mid - 1

        return -1
        