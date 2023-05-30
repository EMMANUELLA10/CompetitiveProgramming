num = int(input("please input a number"))

if num % 2 == 0 and num >= 2 and num <= 5:
    print("not weird")
elif num % 2 == 0 and num >= 6 and num <=20:
    print("weird")
elif num % 2 == 0 and num > 20:
    print("not weird")
else:
    print("weird")