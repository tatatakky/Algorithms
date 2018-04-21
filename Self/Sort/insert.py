# usr/bin/env python
# -*- coding:utf-8 -*-
def insert(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] >= arr[j-1]:
                break
            else:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr

li=[9,1,6,4,9,2,7,4,5,3,8]
print(li)
print(insert(li))

# 名称	      平均計算時間	最悪計算時間	メモリ使用量	安定性
# 挿入ソート	  O(n^2)	    O(n^2)	     O(1)	   安定
