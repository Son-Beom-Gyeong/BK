num1 = int(input("수 입력"))
num2= int(input("수 입력"))
num3 = int(input("수 입력"))

if num1 > num2 :
    if num1 > num3 :
        print("%s이 가장크다"  %num1)
    elif num2 > num3 :
        print("%s이 가장크다" %num2)
if num3 > num1:
    if num3 > num2 :
        print("%s이 가장크다" %num3)
    
