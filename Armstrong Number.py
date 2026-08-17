num = int(input("Enter number : " )
real = num
modi_num= 0
while num != 0:
    rem = num % 10
    modi_num += rem*rem*rem
    num //= 10

if modi_num == real:
    print(True)
else:
    print(False)
