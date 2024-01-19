"""
1. 其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
2. 由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
"""

from typing import List


def radix_sort(arr: List[int]):
    n = len(str(max(arr)))  # 记录最大值的位数
    for k in range(n):  # n轮排序
        # 每一轮生成10个列表
        bucket_list = [[] for i in range(10)]  # 因为每一位数字都是0~9，故建立10个桶
        for i in arr:
            # 按第k位放入到桶中
            bucket_list[i // (10 ** k) % 10].append(i)
        # 按当前桶的顺序重排列表
        arr = [j for i in bucket_list for j in i]
    return arr


# 测试数据

if __name__ == '__main__':
    import random

    random.seed(54)
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    arr_new = radix_sort(arr)
    print("计数排序结果为：", arr_new)
