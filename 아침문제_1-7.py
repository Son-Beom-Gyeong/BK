score = 0
arr=[]
while True :
    score = int(input("수학 점수 기입 \n종료시 111기입"))
    if score == 111 :
        print("종료되었습니다")
        break
    arr.append(score)
    print(set(arr))
    
