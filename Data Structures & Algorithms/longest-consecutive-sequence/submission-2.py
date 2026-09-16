class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        res = 0
        for num in nums:
            if seen[num]:
                continue
            length = seen[num-1] + seen[num+1] + 1
            seen[num] = length
            seen[num - seen[num-1]] = length
            seen[num + seen[num+1]] = length
            res = max(res, length)

        return res
