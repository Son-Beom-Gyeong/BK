height = int(input("공 높이"))
i=0
while height > 0.00001 :
    i +=1
    height = height/2
    
    if height < 0.00001 :
        print(i)
        
        break
