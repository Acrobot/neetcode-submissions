class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l_idx, r_idx = 0, len(nums)-1

        while l_idx < r_idx:
            left_num, right_num = nums[l_idx], nums[r_idx]

            if left_num + right_num == target:
                return [l_idx+1, r_idx+1]
            elif left_num + right_num > target:
                r_idx -= 1
            else:
                l_idx += 1

        return False
        