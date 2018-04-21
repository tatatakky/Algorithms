def sellect(arr):
    for i in range(len(arr)-1):
        mini_index=arr[i:].index(min(arr[i:]))
        arr[i],arr[i+mini_index]=arr[i+mini_index],arr[i]
    return arr

li=[9,1,6,4,9,2,7,4,5,3,8]
print(sellect(li))

# 名称	      平均計算時間  最悪計算時間  メモリ使用量	安定性
# 選択ソート	  O(n^2)	   O(n^2)	 O(1)	    安定ではない
