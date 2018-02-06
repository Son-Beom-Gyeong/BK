arr=[]
a=[]
b=[]
while True :
    
    q = (input("arr에 들어갈 알파벳을 기입하십시오"))
    if q == "" :
        print("종료되었습니다")
        break
    arr.append(q)
while True :    
    w = input("a에 들어갈 알파벳을 기입하십시오")
    if w == "" :
         print("종료되었습니다")
         break
    a.append(w)
while True :   
    e = input("b에 들어갈 알파벳을 기입하십시오")
    if e == "" :
         print("종료되었습니다")
         break

    b.append(e)

i = a+b


for k in range(0, len(i)) :
    if i[k] in arr:
         arr.remove(i[k])
print(arr)

    

