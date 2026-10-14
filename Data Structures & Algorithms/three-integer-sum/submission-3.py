class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = set()

        for i, num in enumerate(nums[:-2]):
            l = i + 1
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] > -num:
                    r -= 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                else:
                    triplets.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                

        return list(triplets)
        