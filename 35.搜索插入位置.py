#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l + 1 if nums[l] < target else l


# @lc code=end
