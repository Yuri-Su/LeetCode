# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        trans_num = 0
        a = x
        while(a > trans_num):
            a, b = divmod(a, 10)
            trans_num = trans_num*10 + b
        return (trans_num == a) or (a == trans_num // 10)
