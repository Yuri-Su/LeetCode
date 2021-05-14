# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         num = len(height)
#         container = [[0 for _ in range(num)] for _ in range(num)]
#         max = 0
#         for i in range(num-1):
#             for j in range(i+1, num):
#                 container[i][j] = (j-i) * min(height[i], height[j])
#                 max = max if container[i][j] <= max else container[i][j]
#         return max
# 双指针法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        num = len(height)
        i = 0
        j = num-1
        max = 0
        while i < j:
            max = min(height[i], height[j]) * \
                (j-i) if min(height[i], height[j])*(j-i) > max else max
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max
