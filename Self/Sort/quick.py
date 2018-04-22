# usr/bin/env python
# -*- coding:utf-8 -*-
def quick(arr):
    if len(arr) in (0,1):
        return arr
    p=arr[-1]
    l=[x for x in arr[:-1] if x <= p]
    r=[x for x in arr[:-1] if x > p]
    return quick(l) + [p] + quick(r)

li=[9,1,6,4,9,2,7,4,5,3,8]
print(li)
print(quick(li))

#     名称	     平均計算時間	   最悪計算時間	メモリ使用量	   安定性
# クイックソート	   O(nlog⁡n)	   O(n^2)	   O(log⁡n)	    安定ではない
