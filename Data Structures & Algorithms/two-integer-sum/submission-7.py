class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {num: idx for idx, num in enumerate(nums)}

        for idx, num in enumerate(nums):
            diff = target - num

            if diff in indices and indices[diff] != idx:
                return [idx, indices[diff]]
        