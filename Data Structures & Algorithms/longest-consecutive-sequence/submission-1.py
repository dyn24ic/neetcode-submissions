class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in setnums:
                maximal = 1
                while i + 1 in setnums:
                    maximal += 1
                    i += 1
                res = max(maximal, res)

        return res
        