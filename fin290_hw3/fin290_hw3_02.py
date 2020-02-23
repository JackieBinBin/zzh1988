# Write python code that reads the text document and counts the unique words
# and stores the words and counts into a dictionary

word_count = {} # 定义字典变量

with open('C:\\Users\\Gary\\Desktop\\zzh\\dracula.txt') as f:
    for word in f.read().split():#读文件并过滤掉空格
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

# 以上with open() as 的用法，可在程序异常报错时，close文件句柄，这样可以不用占内存
# 即可以不用单独close文件；

# Write the words and counts into a text file called ‘dracula words.txt’ by using
# the Python file handle method seen in class.

with open('C:\\Users\\Gary\\Desktop\\zzh\\dracula_words.txt','w+') as f:
        for word,value in word_count.items():
            f.write(word + " : " + str(value)) # 这里要求的是字符串，所以做了字符串组合
            f.write("\n")

# Generate a list called ‘sorted counts’ that contains the value and key pairs as tuples
# that are sorted in descending order based on the frequencies of the words.

sorted_counts = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Output the top 10 most frequently occurring words

for k, v in sorted_counts[:10]:
    print(k, v)

