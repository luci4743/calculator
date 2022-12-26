from tkinter import *
import time
# import tkinter.font as tkFont
from tkinter import messagebox
import sys

expression=""

# take input 
def press(num):
    global expression
    expression+=num
    upd_display.set(expression)
    print(expression)


# calculation

def total():
    try:
        global expression
        temp_expr=str(eval(expression))
        expression=""
        upd_display.set(temp_expr)
        expression+=temp_expr
        print(expression)

    except:
        expression="error"
        upd_display.set(expression)


    


# clear the whole expression
def clear():
    global expression
    expression=""
    upd_display.set("")
    print(expression)



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
    print(expression)
    

def update_dis():
    global expression
    upd_display.set(expression)

def back_key(event):
    # global expression
    # temp_expression=""
    # remove_last_element=len(expression)-1
    # for index in range(0,remove_last_element):
    #     temp_expression+=expression[index]
    # expression=""
    # expression+=temp_expression
    # upd_display.set(expression)
    # print(expression)
    # update_dis()
    back() 


# keybind for execute calculation
def total_key(event):
    # global expression
    # temp_expr=str(eval(expression))
    # expression=""
    # upd_display.set(temp_expr)
    # expression+=temp_expr
    # print(expression)
    total()   #many lines of code saved

 
def escape(event):
    exit_variable=messagebox.askokcancel(title="Exit the application",message="Do you want to exit?",)
    if exit_variable==True:
        sys.exit()
    else:
        pass


 

  

# window creation
root=Tk()
root.title("Calculator")
root.config(bg="black",)

# window.geometry("650x700")

upd_display=StringVar()  #gives access to entry to display and update the numbers


# contained in frame to make ui a little resposive 
window=Frame(root,bg="#212121",)
window.config()
window.pack()

# display of expression
display=Entry(window,textvariable=upd_display,font=("Helvetica",35),bg="#212121",fg="light green",width=20,justify=RIGHT)
display.insert(0,"0")
display.grid(row=0,column=0,columnspan=4,)


# keybinds for lazy people like me
root.bind("<BackSpace>",back_key)
root.bind("<Return>",total_key)
root.bind("<Escape>",escape)

# number buttons

button_9=Button(window,text=9,command=lambda:press("9"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_9.grid(row=2,column=1)

button_8=Button(window,text=8,command=lambda:press("8"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_8.grid(row=2,column=0)

button_7=Button(window,text=7,command=lambda:press("7"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_7.grid(row=3,column=2)

button_6=Button(window,text=6,command=lambda:press("6"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_6.grid(row=3,column=1)

button_5=Button(window,text=5,command=lambda:press("5"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_5.grid(row=3,column=0)

button_4=Button(window,text=4,command=lambda:press("4"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_4.grid(row=4,column=2)

button_3=Button(window,text=3,command=lambda:press("3"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_3.grid(row=4,column=1)

button_2=Button(window,text=2,command=lambda:press("2"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_2.grid(row=4,column=0)

button_1=Button(window,text=1,command=lambda:press("1"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_1.grid(row=5,column=2)

button_0=Button(window,text=0,command=lambda:press("0"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_0.grid(row=5,column=1)

button_dot=Button(window,text=".",command=lambda:press("."),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_dot.grid(row=5,column=0)



# # operations and special buttons
button_add=Button(window,text="+",command=lambda:press("+"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_add.grid(row=3,column=3)

button_subt=Button(window,text="-",command=lambda:press("-"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_subt.grid(row=2,column=3)

button_mul=Button(window,text="X",command=lambda:press("*"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_mul.grid(row=1,column=3)

button_div=Button(window,text="/",command=lambda:press("/"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_div.grid(row=1,column=2)

button_exponent=Button(window,text="^",command=lambda:press("**"),height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_exponent.grid(row=1,column=1)



button_total=Button(window,text="=",command=total,height=3,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_total.grid(row=4,rowspan=5,column=3)


button_clear=Button(window,text="AC",command=clear,height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_clear.grid(row=1,column=0)

button_back=Button(window,text="CE",command=back,height=1,width=6,bg="#212121",fg="white",font=("helvatica",25))
button_back.grid(row=2,column=2)

root.mainloop()