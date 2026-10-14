class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [1] * (len(nums) + 1)
        product_right = [1] * (len(nums) + 1)

        for idx, n in enumerate(nums):
            product_left[idx+1] = n * product_left[idx]
        
        for idx, n in enumerate(nums[::-1]):
            product_right[len(nums)-idx-1] \
                = n * product_right[len(nums)-idx]

        products = []
        for idx in range(len(nums)):
            products.append(product_left[idx] * product_right[idx+1])

        return products
        