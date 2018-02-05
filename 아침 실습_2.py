num1 = int(input("수 입력"))
num2 = int(input("수 입력"))
num3 = int(input("수 입력"))
i = num1 + num2 + num3
if i % 2 == 0 :
    if num1 > num2 :
        if num1 > num3 :
            print("%s 가 큰수" %num1)
    if num2 > num1 :
        if num2 > num3 :
            print("%s 가 큰수" %num2)
            
    if num3 > num1 :
        if num3 > num2 :
            print("%s 가 짝수이면서 큰수" %num3)
else :
    print(i) 
