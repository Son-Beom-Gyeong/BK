product = {'비누', '칫솔', '샴푸','치약','로션'}
sale = {'칫솔', '치약','로션'}
customer = {'칫솔','치약'}
good = customer
bad = {'비누','샴푸'}
p = input("상품을 입력")
if p in bad :
    
    print("판매중지 상품입니다")

print("우수제품은 %s 입니다"  %(good))


    
