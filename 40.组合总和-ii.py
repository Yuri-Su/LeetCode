#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        def backtrack(temp, cur, index):
            if cur == target:
                res.append(temp)
            if cur > target:
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]: continue
                backtrack(temp + [candidates[i]], cur + candidates[i], i+1)

        res = []
        candidates.sort()
        n = len(candidates)
        backtrack([], 0, 0)
        return res


# @lc code=end
