N=input('please enter a number')
if N<='1' or not N.isdigit():  #  isdigit() 方法检测字符串是否只由数字组成
    print('it is not a1 prime number')
else:
    for i in range(2, int(N)+1):
        for j in range (2,int(N)):
            if i % j == 0:
                    print(f' {i} it is not a2 prime number')
            else:
                    print(f' {i} it is a prime number')