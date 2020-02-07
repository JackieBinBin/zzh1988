N = input('please enter a number: ')
while True:
    try:
        N = int(N)
        if N <= 1:
                print('it is not a prime number')
        else:
            for i in range(2, N):
                if N % i == 0:
                    print('it is not a prime number')
                    break
                else:
                    print(i)
                    for j in range(2,i):
                        if N % i==0:
                            break
                        else:
                            print(j)

        break
    except:
        print("you did not enter a prime number")
