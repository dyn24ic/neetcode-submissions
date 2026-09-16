class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l < len(numbers):
            search = target - numbers[l]
            for r in range(l, len(numbers)):
                if numbers[r] == search:
                    return [l+1, r+1]
            l += 1