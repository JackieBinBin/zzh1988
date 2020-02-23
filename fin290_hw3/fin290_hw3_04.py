# Write a program to look for lines of the form :New Revision: 39772
# Extract the number from each of the lines
# Compute the average of the numbers and print out the average

import re

New_Revision_count_mbox = 0
New_Revision_count_mbox_list = []
New_Revision_count_mbox_short = 0
New_Revision_count_mbox_short_list = []

# 生产一个匹配邮件地址的表达式
# \w 标识匹配字母数字或者下划线 + 标识匹配一次或者多次 * 匹配0次或者多次
patternre = re.compile(r"(New Revision: \d+)")

# 匹配mbox文件
with open('C:\\Users\\Gary\\Desktop\\zzh\\mbox.txt') as f:

    New_Revision_count_mbox_list = list(map(lambda revision:revision.replace("New Revision: ",""),patternre.findall(f.read())))
    for num in New_Revision_count_mbox_list:
        New_Revision_count_mbox += int(num)

# 匹配mbox-short文件
with open('C:\\Users\\Gary\\Desktop\\zzh\\mbox-short.txt') as f:
    New_Revision_count_mbox_short_list = list(map(lambda number:number.replace("New Revision: ",""),patternre.findall(f.read())))
    for num in New_Revision_count_mbox_short_list:
        New_Revision_count_mbox_short += int(num)

print(f'Enter file:mbox.txt')
print(f'{New_Revision_count_mbox/len(New_Revision_count_mbox_list)}')


print(f'Enter file:mbox-short.txt')
print(f'{New_Revision_count_mbox/len(New_Revision_count_mbox_short_list)}')