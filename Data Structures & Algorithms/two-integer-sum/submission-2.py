class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = defaultdict(int) #rem -> idx
        for idx, num in enumerate(nums):
            if num not in cache:
                cache[target-num] = idx
            else:
                return [cache[num], idx]