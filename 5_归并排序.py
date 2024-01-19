"""
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；

2.设定两个指针，最初位置分别为两个已经排序序列的起始位置；

3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；

4.重复步骤 3 直到某一指针达到序列尾；

5.将另一序列剩下的所有元素直接复制到合并序列尾。
"""


def mergeSort(arr):
    import math
    if len(arr) < 2:
        return arr
    mid = math.floor(len(arr)/2)
    left = arr[0:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    print(mergeSort(array))
