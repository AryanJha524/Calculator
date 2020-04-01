from tkinter import *

# FIX: AFTER divide by zero, clear everything, it saves the number you divided by zero and uses it as first num for next input
# quick solution i aint even try: check if e.get == "error divide bt 0" and if it does, clear it up?? still gotta figure last part of ^^

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def isnum(first_num):
    try:
        float(first_num)
        return True
    except ValueError:
        return False


def button_click(number):
    global equal_check
    if(isnum(e.get())):
        if equal_check:
            e.delete(0, END)
            e.insert(0, str(number))
            equal_check = False
        else:
            curr = e.get()
            e.delete(0, END)
            # make sure these are strings so they don't add.
            e.insert(0, str(curr) + str(number))
    else:
        e.delete(0, END)
        e.insert(0, str(number))


def button_clear():
    e.delete(0, END)


def add():
    getnum()
    global operation
    operation = "+"


def subtract():
    getnum()
    global operation
    operation = "-"


def multiply():
    getnum()
    global operation
    operation = "*"


def divide():
    getnum()
    global operation
    operation = "/"


def getnum():
    first_num = e.get()
    global f_num
    f_num = float(first_num)
    e.delete(0, END)
    return


def equals():
    global equal_check
    second_num = float(e.get())
    if operation == "+":
        e.delete(0, END)
        e.insert(0, f_num + second_num)
    elif operation == "-":
        e.delete(0, END)
        e.insert(0, f_num - second_num)
    elif operation == "*":
        e.delete(0, END)
        e.insert(0, f_num * second_num)
    elif operation == "/" and second_num != 0:
        e.delete(0, END)
        e.insert(0, f_num / second_num)
    elif operation == "/" and second_num == 0:
        e.delete(0, END)
        e.insert(0, str("Error, divide by 0"))
    equal_check = True  # we have displayed an answer to the screen, so the next time we input a number,
    # we must clear the answer


# Defining buttons

button_1 = Button(root, text="1", padx=40, pady=20, width=3, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, width=3, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, width=3, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, width=3, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, width=3, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, width=3, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, width=3, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, width=3, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, width=3, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, width=3, command=lambda: button_click(0))

# only need lambda if you are going to pass something into the button command.
button_add = Button(root, text="+", padx=40, pady=20, width=3, command=add)
button_subtract = Button(root, text="-", padx=40, pady=20, width=3, command=subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, width=3, command=multiply)
button_divide = Button(root, text="÷", padx=40, pady=20, width=3, command=divide)
button_clear = Button(root, text="Clear", padx=40, pady=20, width=3, command=button_clear)
button_equal = Button(root, text="=", padx=40, pady=20, width=3, command=equals)

# Put buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=1, column=3)
button_add.grid(row=5, column=3)
button_subtract.grid(row=4, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=2, column=3)
button_equal.grid(row=5, column=2)

root.mainloop()
