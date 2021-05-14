class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        # 遍历,多向后看一位
        num = 0
        length = len(s)
        for i in range(length):
            if i+1 < length and dict.get(s[i]) < dict.get(s[i+1]):
                num -= dict.get(s[i])
            else:
                num += dict.get(s[i])
        return num
