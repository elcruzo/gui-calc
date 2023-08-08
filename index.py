import tkinter as tk

calculation = ""

def add_to_calculation():
    global calculation
    calculation += (symbol)
    text_result.delete(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.

    except: 
        pass

def clear_field():
    pass

root = tk.Tk()
root.geometry("300x275")

text_result - tk.Text(root, height=2, width=16 font=("Arial", 24))
text_result.grid(columnspan=5)

root.mainloop()