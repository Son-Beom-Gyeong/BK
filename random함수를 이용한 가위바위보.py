import random

사람1 = int(random.randrange(1, 6))
사람2 = int(random.randrange(1, 6))

if (사람1 > 사람2) :
        print("사람1이 %d, 사람2가 %d로 사람 1이 이겼습니다." %(사람1, 사람2))

elif (사람1 <사람2) :
        print("사람1이 %d, 사람2가 %d로 사람 2가 이겼습니다." %(사람1, 사람2))

else :
              print("비겼습니다")
       
