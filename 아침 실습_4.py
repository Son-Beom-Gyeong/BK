
개수=0
fruit=[]
cost = 0
while True :

    fruit = input("어느 과일을 사실 것 인가요?\n(다 샀다면 엔터)")
    if fruit == "" :
        print("종료 되었습니다")
        break
    개수 = int(input("얼마나 사실 것인가요?"))

    if fruit == '사과' :
             cost= 1000*개수

    if fruit == '포도' :
            if 개수 < 3 :
                cost= 3000*개수
            else :
                cost= 3000*개수*0.9

    if fruit == '귤' :
             cost= 500*개수
             개수 = 개수 + (개수//10) *2
             
    if fruit == '배' :
             cost= 2000*개수

    print("귀하는 %s -> %s 금액 %s" %(fruit, 개수, cost))
             
