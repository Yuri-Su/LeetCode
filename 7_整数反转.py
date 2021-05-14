class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        while x:
            tmp = x
            x = tmp // 10 if tmp >= 0 else int(tmp / 10) # 负数向上取整，正数向下取整
            carry = tmp % 10 if tmp >= 0 else tmp % (-10)
            if (num > MAX // 10) or (num == MAX // 10 and carry > 7):
                return 0
            
            if (num < int(MIN / 10)) or (num == int(MIN / 10) and carry < -8):
                return 0
                
            num = num * 10 + carry
        
        
        return num
            