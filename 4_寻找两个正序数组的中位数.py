# 二分查找
# 假设两个有序数组分别是 A 和 B。要找到第 k 个元素，我们可以比较 A[k/2−1] 和 B[k/2−1]
# 由于 A[k/2−1] 和 B[k/2−1] 的前面分别有 A[0..k/2−2] 和 B[0..k/2−2]，即 k/2-1k/2−1 个元素，
# 对于 A[k/2−1] 和 B[k/2−1] 中的较小值，最多只会有 (k/2−1)+(k/2−1)≤k−2 个元素比它小，那么它就不能是第 k 小的数了。

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)

        def get_kth_element(k: int) -> int:
            i1, i2 = 0, 0
            while k != 0:
                if i1 == n1:
                    return nums2[i2 + k - 1]    #只有第二个数组
                if i2 == n2:
                    return nums1[i1 + k - 1]
                if k == 1:                              #1//2 = 0 所有也要判断一下
                    return min(nums1[i1], nums2[i2])

                new_i1 = min(i1 + k//2 - 1, n1 - 1)                  #每个数组贡献 k//2  可能数组中没有k//2个元素
                new_i2 = min(i2 + k//2 - 1, n2 - 1)
                pivot_1, pivot_2 = nums1[new_i1], nums2[new_i2]
                if pivot_1 <= pivot_2:                  #把小的那段扔掉
                    k -= (new_i1 - i1 + 1)              #做好index的更新
                    i1 = new_i1 + 1
                else:
                    k -= (new_i2 - i2 + 1)
                    i2 = new_i2 + 1

        n = n1 + n2
        if n % 2 == 1:
            return get_kth_element( (n+1) // 2 )    # 0 1 2 3 4  n=5 取第3个
        else:
            return ( get_kth_element( n//2 ) + get_kth_element( (n+2)//2 ) ) / 2.0  # 0 1 2 3 n=4 取第2个，第3个的aver