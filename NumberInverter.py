while True:
    num = int(input("Enter a number: "))
    rev_num = 0
    while num > 0:
        remainder = num % 10
        rev_num = (rev_num * 10) + remainder
        num = num // 10
    if -2147483648 > num < 2147483647:
        print("0")    
    print(rev_num)