class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                # 栈是空的或者栈顶元素不匹配
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # 匹配,弹出
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack