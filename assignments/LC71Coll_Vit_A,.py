menuList=[]
priceList=[]

def showBill():
    temp = 0
    print("-----My Shop-----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
         temp += int(priceList[number])
    print("Total : ",temp)
while True:
    menuName=input("Please Enter :")
    if(menuName.lower()=="exit"):
        break
    else:
        menuPrice=input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
