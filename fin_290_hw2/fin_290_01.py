x=99;y=77;z=101

zzh = [x, y, z]


# enumerate(zzh) 是根据zzh 这个list返回一个键值序列对
# 像这样 [(0, x),(1,y),(2,z)]，我后续操作都是对索引来的(0,1,2)，
# 目的就是为了在排序后能追踪到原始数据，
# 相当于我没动原始数据zzh,只是找出了所有奇数并排序，
# =======================

# 这是个列表推导式，i for i in enumerate(zzh) if i[1]%2
# 目的是过滤出odd 数据，并重组为新的奇数列表：sorted_odd_nums
# ====================

sorted_odd_nums = sorted((i for i in enumerate(zzh) if i[1]%2),
                         key = lambda i:i[1],
                         reverse=True)

print(sorted_odd_nums) # 这个为奇数列表


if not sorted_odd_nums:
    pass
# all numbers were even and filtered out.
elif sorted_odd_nums[0][0] == 0:
    print("x is the largest odd number")
elif sorted_odd_nums[0][0] == 1:
    print("y is the largest odd number")
elif sorted_odd_nums[0][0] == 2:
    print("z is the largest odd number")