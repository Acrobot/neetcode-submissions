class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers)-1

        while numbers[i1] + numbers[i2] != target:
            if numbers[i1] + numbers[i2] > target:
                i2 -= 1
            else:
                i1 += 1

        return [i1+1, i2+1]
            
        