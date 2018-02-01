메뉴 = input("메뉴를 입력해주세요")

coffee = {"Americano" : 2000,
          "Cafe latte" : 2500,
          "Green Tea latte" : 3000,
          "Mocha latte" : 3500}

if 메뉴 in list(coffee.keys()) :
    print(True)

else :
    print(False)
