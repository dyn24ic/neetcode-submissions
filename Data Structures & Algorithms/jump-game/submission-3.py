class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = {}

        goal = len(nums) - 1
        def dfs(i):

            if i in memo:
                return memo[i]

            if i == goal:
                return True

            # dead branch
            if nums[i] == 0:
                return False

            end = min(len(nums), i + nums[i] + 1)

            for j in range(i + 1, end):
                if dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)