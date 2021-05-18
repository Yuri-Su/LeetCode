#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# 贪心
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:

        step, end, maxP = 0, 0, 0
        n = len(nums)
        for i in range(n - 1):
            maxP = max(maxP, i + nums[i])
            # nums[i]记录往后走的步数
            # 当i == end时，刚好记录了下一步中跳到最远的i
            if i == end:
                end = maxP
                step += 1
        return step


# @lc code=end
