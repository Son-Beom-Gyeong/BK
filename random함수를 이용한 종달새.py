import random

시간 = int(random.randrange(0, 24))
날씨 = random.choice([True, False])


print("시간은 = %d" %시간)
print("날씨는 = %d" %날씨)
if 시간 == 6 and 날씨 == True :
    print("종달새가 노래를 부르고있다")

else :
    print("종달새가 노래를 부르지 않습니다")
