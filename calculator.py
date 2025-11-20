import tkinter as tk

# create main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

# update the display
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# evaluate the expression
def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# clear the display
def clear():
    global expression
    expression = ""
    equation.set("")

# display field
equation = tk.StringVar()
display = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, relief="sunken")
display.grid(columnspan=4, ipadx=10, ipady=20)

# buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=8, height=3, command=equal)
    else:
        btn = tk.Button(root, text=text, width=8, height=3,
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# clear button
clear_btn = tk.Button(root, text="CLEAR", width=34, height=3, command=clear)
clear_btn.grid(row=5, columnspan=4)

# run application
root.mainloop()
