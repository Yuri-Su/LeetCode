#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height)

        sum = 0
        maxleft = [0] * n
        maxright = [0] * n
        maxleft[0] = height[0]
        maxright[n - 1] = height[n - 1]
        for i in range(1, n):
            maxleft[i] = max(maxleft[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], height[i])
        for i in range(n):
            sum += min(maxleft[i], maxright[i]) - height[i]
        return sum


# @lc code=end
