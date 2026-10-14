class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_left = []
        prod_right = []

        current_prod = 1
        for num in nums:
            prod_left.append(current_prod)
            current_prod *= num

        current_prod = 1
        for num in reversed(nums):
            prod_right.append(current_prod)
            current_prod *= num

        num_count = len(nums)
        out = []
        for idx in range(num_count):
            out.append(prod_left[idx] * prod_right[num_count - idx - 1])

        return out

        
        