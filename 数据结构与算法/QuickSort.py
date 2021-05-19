"""
快速排序
一次遍历后k会到达他所在位置
"""


class solution():
    def quick_sort(self, lists, i, j):
        if i >= j:
            return list
        pivot = lists[i]
        low = i
        high = j
        while i < j:
            while i < j and lists[j] >= pivot:
                j -= 1
            lists[i] = lists[j]
            while i < j and lists[i] <= pivot:
                i += 1
            lists[j] = lists[i]
        lists[j] = pivot
        self.quick_sort(lists, low, i - 1)
        self.quick_sort(lists, i + 1, high)
        return lists


if __name__ == "__main__":
    s = solution()
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print("排序前的序列为：")
    for i in lists:
        print(i, end=" ")
    print("\n排序后的序列为：")
    for i in s.quick_sort(lists, 0, len(lists) - 1):
        print(i, end=" ")
