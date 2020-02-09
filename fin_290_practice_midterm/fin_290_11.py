# Write code to remove the commas in the following string: ‘ab,cd,ef,gh,i’.

s = 'ab,cd,ef,gh,i'

s1 = s.replace(',','') # 这里replace方法不改变原有s字符串的值，所以要赋值一下

print(s1)

# Write code that pulls the words out of the string and places them into a list
# without the punctuations:
# 即跟fin_290_03 题有点像

s2 = 'Can?? You!! Pull only?! the,, words.. out of!! this Sentence??!!'

word_list = [] # 初始化字符串列表
word_string = '' # 初始化字符串中间值

for i in s2:
    if i =='?' or i == '!' or i == ',' or i == '.':
        continue
    elif i != ' ':
        word_string += i
    else:
        word_list.append(word_string)
        word_string = ''

word_list.append(word_string)
print(word_list)