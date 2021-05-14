class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        nums.sort()
        for i in range(n-2):
            # 判断一下如果当前元素和上一个元素相等则跳出本次循环
            if i > 0 and nums[i] == nums[i-1]:   # i=0的时候我们需要直接往下执行
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: # 重复数字不需要考虑
                        l += 1
                    while l < r and nums[r] == nums[r+1]: # 重复数字不需要考虑
                        r -= 1
                elif tmp > 0: # 说明需要一个更小的数字
                    r -= 1
                else: # 说明需要一个更大的数字
                    l += 1
        return res