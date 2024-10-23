import tkinter as tk
import math
from tkinter import Button
calculation = ""
# Below are the functions for calculating, evaluating/=, and clearing the field
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")



# GUI size and return
root = tk.Tk()
root.geometry("470x300")
# GUI Nunber size and output size
text_result =tk.Text(root, height = 2, width = 32, font = ("Arial", 24))
text_result.grid(columnspan = 5)
# Everything below defines and makes a button for each variable
btn_1 = tk.Button(root, text ="1", command=lambda: add_to_calculation(1), width = 10, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text ="2", command=lambda: add_to_calculation(2), width = 10, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text ="3", command=lambda: add_to_calculation(3), width = 10, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text ="4", command=lambda: add_to_calculation(4), width = 10, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text ="5", command=lambda: add_to_calculation(5), width = 10, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text ="6", command=lambda: add_to_calculation(6), width = 10, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text ="7", command=lambda: add_to_calculation(7), width = 10, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text ="8", command=lambda: add_to_calculation(8), width = 10, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text ="9", command=lambda: add_to_calculation(9), width = 10, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_10 = tk.Button(root, text ="0", command=lambda: add_to_calculation(0), width = 10, font=("Arial", 14))
btn_10.grid(row=5, column=1)
btn_11 = tk.Button(root, text ="//", command=lambda: add_to_calculation("//"), width = 10, font=("Arial", 14))
btn_11.grid(row=5, column=2)
btn_12 = tk.Button(root, text ="=", command=evaluate_calculation, width = 10, font=("Arial", 14))
btn_12.grid(row=5, column=3)
btn_13 = tk.Button(root, text ="+", command=lambda: add_to_calculation("+"), width = 10, font=("Arial", 14))
btn_13.grid(row=5, column=4)
btn_14 = tk.Button(root, text ="-", command=lambda: add_to_calculation("-"), width = 10, font=("Arial", 14))
btn_14.grid(row=4, column=4)
btn_15 = tk.Button(root, text ="*", command=lambda: add_to_calculation("*"), width = 10, font=("Arial", 14))
btn_15.grid(row=3, column=4)
btn_16 = tk.Button(root, text ="/", command=lambda: add_to_calculation("/"), width = 10, font=("Arial", 14))
btn_16.grid(row=2, column=4)
btn_17 = tk.Button(root, text ="^", command=lambda: add_to_calculation("**"), width = 8, font=("Arial", 14))
btn_17.grid(row=6, column=1)
btn_18 = tk.Button(root, text ="π", command=lambda: add_to_calculation(math.pi), width = 8, font=("Arial", 14))
btn_18.grid(row=6, column=2)
btn_19 = tk.Button(root, text ="CE", command=lambda: clear_field(), width = 8, font=("Arial", 14))
btn_19.grid(row=6, column=3)
btn_19 = tk.Button(root, text =".", command=lambda: add_to_calculation("."), width = 8, font=("Arial", 14))
btn_19.grid(row=6, column=4)
root.mainloop()