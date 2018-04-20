# usr/bin/env python
# -*- coding:utf-8 -*-

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1,i,-1): #10からiまで1ずつ減る
            # print(j-1,j)
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            print(arr)
    return arr

li=[9,1,6,4,9,2,7,4,5,3,8]
print(li)
print(bubble(li))

#
# 名称         平均計算時間  最悪計算時間  メモリ使用量	安定性
# バブルソート	 O(n^2)	      O(n^2)	   O(1)	      安定
