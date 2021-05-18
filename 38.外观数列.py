#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        if n == 1: return s
        pre = s
        for _ in range(1,n):
            temp = ''
            pre_length = len(pre)
            count = 1
            i = 0
            while i + 1 < pre_length:
                if pre[i] == pre[i + 1]:
                    count += 1
                if pre[i] != pre[i + 1]:
                    temp += str(count) + str(pre[i])
                    count = 1
                i += 1
            if i + 1 == pre_length: temp += str(count) + str(pre[i])
            pre = temp
        return pre


# @lc code=end
