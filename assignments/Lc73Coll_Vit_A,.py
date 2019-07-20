menuList=[]
def showBill():
    temp = 0
    print("-----My Shop-----")
    for number in range(len(menuList)):
        print(menuList[number])
        temp+=int(menuList[number][1])
    print("Total :",temp)
while True:
    menuName=input("Please Enter :")
    if(menuName.lower()=="exit"):
        break
    else:
        menuPrice=input("Price :")
        menuList.append([menuName,menuPrice])
showBill()
