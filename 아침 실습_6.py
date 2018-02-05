score=[]
for i in range(0, 6) :    
    score.append(int(input("시험점수 입력")))


score.sort()
print("최고 점수는 %s입니다" %(score[5]))


