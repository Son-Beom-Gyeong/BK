str11 = "진수쌤 완전 동안임~"
print(str11.replace("진수쌤", "최경우"))


str12 = "a-a-a-a-a"
print(str12.replace("a","b"))


ss= '   파 이 썬    '
print(ss.strip())
print(ss.rstrip())
print(ss.lstrip())

ss='-----파---이---썬----'
print(ss.strip('-'))
ss='<<<파 << 이 >> 썬>>>'
print(ss.strip('<>'))
      
str12 = "a/a/a/a/a"
print(str12.split("/"))

print(str12.split("/", 3))

fruits_2 = 'I Like Apple!'
print(len(fruits_2))

ss=input("문자열 입력==>")

print("출력 문자열==>", end= ' ')
for i in range(0, len(ss)) :
    if ss[i]!='o' :
        print(ss[i], end='')
    else :
        print('$', end='')
