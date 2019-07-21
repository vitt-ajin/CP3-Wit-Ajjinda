from tkinter import *
import math

def leftClickButton(even):
    result=float(textBoxWidth.get())/math.pow(float(textBoxHeight.get())/100,2)
    if result>=30.0:
        labelResult.configure(text="อ้วนมาก")
    elif result>=25.0:
        labelResult.configure(text="อ้วน")
    elif result>=23.0:
        labelResult.configure(text="น้ำหนักเกินก")
    elif result>=18.6:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif result<18.6:
        labelResult.configure(text="ผอมเกินไป")
    print(result)
    print(type(result))

mainWindow=Tk()

labelHeight=Label(mainWindow,text="ส่วนสูง (Cm.):")
labelHeight.grid(row=0,column=0)
textBoxHeight=Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)

labelWidth=Label(mainWindow,text="น้ำหนัก (Kg.):")
labelWidth.grid(row=1,column=0)
textBoxWidth=Entry(mainWindow)
textBoxWidth.grid(row=1,column=1)

calculateButton=Button(mainWindow,text="คำนวน")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult=Label(mainWindow,text="ผลลัทพ์")
labelResult.grid(row=2,column=1)

mainWindow.mainloop()