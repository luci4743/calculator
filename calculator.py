from tkinter import *
import time

expression=""

# take input 
def press(num):
    global expression
    expression+=num
    upd_display.set(expression)
    print(expression)


# calculation
def total():
    global expression
    temp=str(eval(expression))
    print(temp)
    expression=""
    upd_display.set(temp)
    expression+=temp


# clear the whole expression
def clear():
    global expression
    expression=""
    upd_display.set("")



# deletes just the last element (check back on this later, there is a probably better way to do this)
def back():
    global expression
    temp_expression=""
    remove_last_element=len(expression)-1
    for index in range(0,remove_last_element):
        temp_expression+=expression[index]
    expression=""
    expression+=temp_expression
    upd_display.set(expression)

# window creation
window=Tk()

upd_display=StringVar()

# display of expression
display=Entry(window,textvariable=upd_display,font=("Ariel",15),bg="#212121",fg="light green")
display.pack()

# numbers
button_1=Button(window,text=1,command=lambda:press("1"))
button_1.pack()

button_2=Button(window,text=2,command=lambda:press("2"))
button_2.pack()

button_3=Button(window,text=3,command=lambda:press("3"))
button_3.pack()

button_4=Button(window,text=4,command=lambda:press("4"))
button_4.pack()

button_5=Button(window,text=5,command=lambda:press("5"))
button_5.pack()

button_6=Button(window,text=6,command=lambda:press("6"))
button_6.pack()

button_7=Button(window,text=7,command=lambda:press("7"))
button_7.pack()

button_8=Button(window,text=8,command=lambda:press("8"))
button_8.pack()

button_9=Button(window,text=9,command=lambda:press("9"))
button_9.pack()

button_0=Button(window,text=0,command=lambda:press("0"))
button_0.pack()



# operations and special buttons
button_add=Button(window,text="+",command=lambda:press("+"))
button_add.pack()

button_subt=Button(window,text="-",command=lambda:press("-"))
button_subt.pack()

button_mul=Button(window,text="X",command=lambda:press("*"))
button_mul.pack()

button_div=Button(window,text="/",command=lambda:press("/"))
button_div.pack()

button_exponent=Button(window,text="^",command=lambda:press("**"))
button_exponent.pack()

button_total=Button(window,text="=",command=total)
button_total.pack()

button_clear=Button(window,text="C",command=clear)
button_clear.pack()

button_back=Button(window,text="<--",command=back)
button_back.pack()

window.mainloop()