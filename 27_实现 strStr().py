class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        i = 0

        while i < n - m + 1:
            temp = i
            j = 0
            while j < m:
                if haystack[temp] != needle[j]:
                    break
                temp += 1
                j += 1
            if j == m:
                return i
            i += 1

        return -1


s = Solution()
print(s.strStr('hello', 'll'))
