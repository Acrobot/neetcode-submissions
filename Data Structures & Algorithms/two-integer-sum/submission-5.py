class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {n: idx for idx, n in enumerate(nums)}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in values and values[remaining] != i:
                return list(sorted([i, values[remaining]]))
        