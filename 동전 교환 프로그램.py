a= int(input("교환할 돈은 얼마 :" ))

b=a//500  
c=a-500*b  
d=c//100   
e=a-500*b-d*100
print(e)
f=e//10
g=e-f*10

print("오백원짜리 ==>" , b)
print("백원짜리 ==>" , d)
print("십원짜리 ==>" , f)
print("바꾸지 못 한돈 ==>" , g)




