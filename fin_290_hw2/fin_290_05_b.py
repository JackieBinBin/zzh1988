# Write a bubble sort algorithm that operates on a list of arbitrary numbers.


zzh_list = [54.11,26,93.1,17,77,31,44,55,20.2]

# for i in range(len(zzh_list)-1): # i 代表需要对比的轮数：len(list)-1
#     j 代表每轮需要比对的元素对象
#     每轮对比的元素个数:len(zzh_list)-i
#     for j in range(1,len(zzh_list)-i):
#         if zzh_list[j-1] > zzh_list[j]:
#             zzh_list[j-1],zzh_list[j] = zzh_list[j],zzh_list[j-1]
#             print(f'round j {j}')
#             print(zzh_list)

# 优化办法：
for num in range(len(zzh_list)-1, 0, -1): # 对比轮数：
    for i in range(num):
        if zzh_list[i] > zzh_list[i+1]:
            zzh_list[i], zzh_list[i+1] = zzh_list[i+1], zzh_list[i]

print(f'finally results')
print(zzh_list)