#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        def backtrack(temp, cur, index):
            if cur == target:
                res.append(temp)
            if cur > target:
                return
            for i in range(index, n):
                backtrack(temp + [candidates[i]], cur + candidates[i], i)

        res = []
        n = len(candidates)
        backtrack([], 0, 0)
        return res


# @lc code=end
