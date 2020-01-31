# Write a bubble sort algorithm that operates on a list of arbitrary numbers.


zzh_list = [54.11,26,93.1,17,77,31,44,55,20.2]

for i in range(len(zzh_list)-1): # i 代表对比轮数：=len(list)-1
    for j in range(1,len(zzh_list)): # j 代表每轮需要比对的元素对象
        if zzh_list[j-1] > zzh_list[j]:
            zzh_list[j-1],zzh_list[j] = zzh_list[j],zzh_list[j-1]
            print(f'round j {j}')
            print(zzh_list)

print(f'finally results')
print(zzh_list)