# Write code that sorts a list of names into alphabetical order

zzh_list = ['paul','tom','terra','Maxwell','Rosemary','Shirley']

# sort函数 默认是by  alphabetical order

zzh_list.sort()

print(zzh_list)

# 根据长度

zzh_list.sort(key=len)

print(zzh_list)
