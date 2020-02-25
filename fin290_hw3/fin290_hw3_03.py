# Write a program to read through a mail log, build a histogram
# using a dictionary to count how many messages have come from each email address,
#  and print the dictionary for both the mbox-short.txt and mbox.txt files

import re

email_count_mbox = {}
email_count_mbox_short = {}

# 生产一个匹配邮件地址的表达式
# \w 标识匹配字母数字或者下划线 + 标识匹配一次或者多次 * 匹配0次或者多次
mailre = re.compile(r"(From \w+\.*\w+@\w+\.*\w+\.*\w+)")

# 匹配mbox文件
with open('C:\\Users\\Gary\\Desktop\\zzh\\mbox.txt') as f:
    # mailre.findall(f.read()) 根据邮件匹配表达式抓内容，返回的是list
    # 这里根据From mailaddress来计数的
    mail_list = map(lambda mail:mail.replace("From ",""),mailre.findall(f.read()))
    for mail in mail_list:
        if mail not in email_count_mbox:
            email_count_mbox[mail] = 1
        else:
            email_count_mbox[mail] += 1

# 匹配mbox-short文件
with open('C:\\Users\\Gary\\Desktop\\zzh\\mbox-short.txt') as f:
    mail_list = map(lambda mail:mail.replace("From ",""),mailre.findall(f.read()))
    for mail in mail_list:
        if mail not in email_count_mbox_short:
            email_count_mbox_short[mail] = 1
        else:
            email_count_mbox_short[mail] += 1

# 根据抓取的内容排序

# Mbox
sorted_counts_mbox = dict(sorted(email_count_mbox.items(), key=lambda x: x[1], reverse=True))

# Mbox—short
sorted_counts_mbox_short = dict(sorted(email_count_mbox_short.items(), key=lambda x: x[1], reverse=True))

print(sorted_counts_mbox_short.values())

#  build a histogram using a dictionary to count how many messages
# have come from each email address

import matplotlib.pyplot as plt

plt.bar(range(len(sorted_counts_mbox_short)), sorted_counts_mbox_short.values(),
        color='rgb', tick_label=sorted_counts_mbox_short.keys())
plt.show()