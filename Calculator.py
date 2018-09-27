from tkinter import *

def calc(numbers):
    global value
    global operator
    operator += str(numbers)
    value.set(operator)

def eq():
    global operator
    sumup = str(eval(operator))
    value.set(sumup)
    operator = ""

def clear():
    global operator
    global value
    value.set("")
    operator = ""

root = Tk()
root.title("CalcuPy")
value = StringVar()
operator = ""
root.minsize(340, 320)
#
textbox = Entry(root, font=("arial", 20, "bold"),text=value, bd=20, insertwidth=4, justify="right").grid(columnspan=4)
btn7 = Button(root, padx=16, pady=10, text="7", bd=8, command=lambda:calc(7)).grid(row=1, column=0)
btn8 = Button(root, padx=16, pady=10, text="8", bd=8, command=lambda:calc(8)).grid(row=1, column=1)
btn9 = Button(root, padx=16, pady=10, text="9", bd=8, command=lambda:calc(9)).grid(row=1, column=2)
btnmin = Button(root, padx=16, pady=10, text="-", bd=8, command=lambda:calc("-")).grid(row=1, column=3)
#
btn4 = Button(root, padx=16, pady=10, text="4", bd=8, command=lambda:calc(4)).grid(row=2, column=0)
btn5 = Button(root, padx=16, pady=10, text="5", bd=8, command=lambda:calc(5)).grid(row=2, column=1)
btn6 = Button(root, padx=16, pady=10, text="6", bd=8, command=lambda:calc(6)).grid(row=2, column=2)
btnplus = Button(root, padx=16, pady=10, text="+", bd=8, command=lambda:calc("+")).grid(row=2, column=3)
#
btn1 = Button(root, padx=16, pady=10, text="1", bd=8, command=lambda:calc(1)).grid(row=3, column=0)
btn2 = Button(root, padx=16, pady=10, text="2", bd=8, command=lambda:calc(2)).grid(row=3, column=1)
btn3 = Button(root, padx=16, pady=10, text="3", bd=8, command=lambda:calc(3)).grid(row=3, column=2)
btmul = Button(root, padx=16, pady=10, text="*", bd=8, command=lambda:calc("*")).grid(row=3, column=3)
#
btn0 = Button(root, padx=16, pady=10, text="0", bd=8, command=lambda:calc(0)).grid(row=4, column=0)
btnC = Button(root, padx=16, pady=10, text="C", bd=8, command=clear).grid(row=4, column=1)
btneq = Button(root, padx=16, pady=10, text="=", bd=8, command=eq).grid(row=4, column=2)
btdiv = Button(root, padx=16, pady=10, text="/", bd=8, command=lambda:calc("/")).grid(row=4, column=3)
#
root.maxsize(340, 400)
root.mainloop()
