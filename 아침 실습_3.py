num2 = int(input("수 입력"))
num1 = int(input("수 입력"))
num3 = int(input("가장 큰 수 입력"))

if num1 + num2 <= num3 :
    print("삼각형이 성립하지 않는다")
else :
    if num2 == num1 == num3 :
        print("정삼각형")
        
    elif num1 == num3 or num1== num2 or num3 == num2 :
        print("이등변삼각형")

    elif num3**2 == num1**2 + num2**2 :
        print("직각삼각형")

    elif num3 <= num1 + num2 :
        print("일반 삼각형")
