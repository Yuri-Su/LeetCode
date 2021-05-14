#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target > nums[-1]:
            return [-1, -1]
        left1 = self.searchFirstPosition(nums, target)
        if target != nums[left1]:
            return [-1, -1]
        return [left1, self.searchFirstPosition(nums, target + 1) - 1] 


    def searchFirstPosition(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left






# @lc code=end

