def merge(list_1, list_2, list):
    n_1, n_2 = len(list_1), len(list_2)
    i1, i2, i = 0, 0, 0
    while i1 < n_1 and i2 < n_2:
        list[i] = list_1[i1] if list_1[i1] < list_2[i2] else list_2[i2]
        i += 1

    while i1 < n_1:
        list[i] = list_1[i1]
        i1 += 1
        i += 1
    while i2 < n_2:
        list[i] = list_2[i2]
        i2 += 1
        i += 1


def mergeSort(nums):
    n = len(nums)

    if n > 1:
        m = n // 2
        mergeSort(nums_1)
        mergeSort(nums_2)
        merge(nums_1, nums_2, nums)
