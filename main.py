import tkinter as tk

count = 0
calculation = ""
variable = ""

def call_to_addition(symbol):
    global count
    global calculation
    global variable
    if count != 17 and symbol in [1,2,3,4,5,6,7,8,9,0]:
        calculation += str(symbol)
        variable += str(symbol)
        text_field.delete(1.0, 'end')
        text_field.insert(1.0, variable)
        count += 1
    elif symbol not in [1,2,3,4,5,6,7,8,9,0]:
        calculation += str(symbol)
        variable = ""
        text_field.delete(1.0, 'end')
        count = 0

def evaluate():
    global calculation
    global count
    try:
        calculation = str(eval(calculation))
        text_field.delete(1.0, 'end')
        text_field.insert(1.0, calculation)
        count = 0
    except:
        clear_field()
        text_field.insert(1.0, 'ERROR')


def clear_field():
    global count
    global calculation
    global variable
    variable = ""
    calculation = ''
    count = 0
    text_field.delete(1.0, 'end')

root = tk.Tk()
root.geometry('328x350')
root.config(bg='pink')

text_field = tk.Text(root, height=2, width=17, font=('Arial', 24))
text_field.grid(columnspan=5, padx=8, pady=4)

btn_1 = tk.Button(root, text='1', bg='white', activebackground='red', command=lambda: call_to_addition(1), width=5 , font=('Arial', 15))
btn_1.grid(row=2, column=0, padx=8, pady=5)
btn_2 = tk.Button(root, text='2', bg='white', activebackground='red', command=lambda: call_to_addition(2), width=5, font=('Arial', 15))
btn_2.grid(row=2, column=1)
btn_3 = tk.Button(root, text='3', bg='white', activebackground='red', command=lambda: call_to_addition(3), width=5, font=('Arial', 15))
btn_3.grid(row=2, column=2)
btn_plus = tk.Button(root, text='+', bg='white', activebackground='red', command=lambda: call_to_addition('+'), width=5, font=('Arial', 15))
btn_plus.grid(row=2, column=3)

btn_4 = tk.Button(root, text='4', bg='white', activebackground='red', command=lambda: call_to_addition(4), width=5, font=('Arial', 15))
btn_4.grid(row=3, column=0, pady=5)
btn_5 = tk.Button(root, text='5', bg='white', activebackground='red', command=lambda: call_to_addition(5), width=5, font=('Arial', 15))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text='6', bg='white', activebackground='red', command=lambda: call_to_addition(6), width=5, font=('Arial', 15))
btn_6.grid(row=3, column=2)
btn_minus = tk.Button(root, text='-', bg='white', activebackground='red', command=lambda: call_to_addition('-'), width=5, font=('Arial', 15))
btn_minus.grid(row=3, column=3)

btn_7 = tk.Button(root, text='7', bg='white', activebackground='red', command=lambda: call_to_addition(7), width=5, font=('Arial', 15))
btn_7.grid(row=4, column=0, pady=5)
btn_8 = tk.Button(root, text='8', bg='white', activebackground='red', command=lambda: call_to_addition(8), width=5, font=('Arial', 15))
btn_8.grid(row=4, column=1)
btn_9 = tk.Button(root, text='9', bg='white', activebackground='red', command=lambda: call_to_addition(9), width=5, font=('Arial', 15))
btn_9.grid(row=4, column=2)
btn_mul = tk.Button(root, text='*', bg='white', activebackground='red', command=lambda: call_to_addition('*'), width=5, font=('Arial', 15))
btn_mul.grid(row=4, column=3)

btn_open = tk.Button(root, text='(', bg='white', activebackground='red', command=lambda: call_to_addition('('), width=5, font=('Arial', 15))
btn_open.grid(row=5, column=0, pady=5)
btn_0 = tk.Button(root, text='0', bg='white', activebackground='red', command=lambda: call_to_addition(0), width=5, font=('Arial', 15))
btn_0.grid(row=5, column=1)
btn_close = tk.Button(root, text=')', bg='white', activebackground='red', command=lambda: call_to_addition(')'), width=5, font=('Arial', 15))
btn_close.grid(row=5, column=2)
btn_div = tk.Button(root, text='/', bg='white', activebackground='red', command=lambda: call_to_addition('/'), width=5, font=('Arial', 15))
btn_div.grid(row=5, column=3)

btn_clear = tk.Button(root, text='C', bg='white', activebackground='red', command=clear_field, width=10, font=('Arial', 15))
btn_clear.grid(row=6, column=0, columnspan=2, pady=5)
btn_equal = tk.Button(root, text='=', bg='white', activebackground='red', command=evaluate, width=10, font=('Arial', 15))
btn_equal.grid(row=6, column=2, columnspan=2)

root.mainloop()
