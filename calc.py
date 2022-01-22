import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

# ============================settings =================================
root = Tk()
root.geometry('400x200')
root.title('calculator')
root.resizable(width=False, height=False)
color = 'gray'
root.configure(bg=color)
# ============================variable =================================
num1 = IntVar()
num2 = IntVar()
res_value = IntVar()

# ================================frames===================================

top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# ================================Functions===================================

def errorMsg(ms):
    if ms == 'error':
        return tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'division zero error':
        return tkinter.messagebox.showerror('Division Error', 'Can Not division By 0')


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        return errorMsg('error')


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg('error')


def div():
    if num2.get() == 0:
        return errorMsg('division zero error')
    try:
        value = float(num1.get()) / float(num2.get())
        res_value.set(value)
    except:
        return errorMsg('error')


# ================================Buttons===================================
btn_plus = Button(top_third, width=10, text='+', highlightbackground=color, command=lambda: plus())
btn_plus.pack(side=LEFT, padx=5, pady=5)

btn_minus = Button(top_third, width=10, text='-', highlightbackground=color, command=lambda: minus())
btn_minus.pack(side=LEFT, padx=10, pady=10)

btn_mul = Button(top_third, width=10, text='*', highlightbackground=color, command=lambda: mul())
btn_mul.pack(side=LEFT, padx=10, pady=10)

btn_div = Button(top_third, width=10, text='/', highlightbackground=color, command=lambda: div())
btn_div.pack(side=LEFT, padx=10, pady=10)
# ================================Entries and Labels===================================
label_first_num = Label(top_first, text='Input Number 1: ', bg=color)
label_first_num.pack(side=LEFT, pady=10, padx=10)

first_num = Entry(top_first, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second, text='Input Number 2: ', bg=color)
label_second_num.pack(side=LEFT, pady=10, padx=10)

second_num = Entry(top_second, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_forth, text='Result: ', bg=color)
res.pack(side=LEFT, pady=10, padx=10)

res_num = Entry(top_forth, highlightbackground=color, textvariable=res_value)
res_num.pack(side=LEFT)

root.mainloop()
