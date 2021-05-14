# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 特殊情况
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

class Solution:
    def intToRoman(self, num: int) -> str:
        # 从大到小排序
        # 例58  50->5->1->1->1
        tmp = (
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
        ret = ""
        for i, j in tmp:
            div = num // i
            if div:
                ret += j * div
                num -= div * i
        return ret