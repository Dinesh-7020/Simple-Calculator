import tkinter as tk

def add():
    result = float(entry1.get()) + float(entry2.get()) 
    label_result.config(text=f"Result: {result}")

def subtract():
    result = float(entry1.get()) - float(entry2.get()) 
    label_result.config(text=f"Result: {result}")

def multiply():
    result = float(entry1.get()) * float(entry2.get()) 
    label_result.config(text=f"Result: {result}")

def divide():
    result = float(entry1.get()) / float(entry2.get()) 
    label_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x350")
root.config(bg="#edf2f4")

# Title label
title = tk.Label(root, text="Simple Calculator", font=('Helvetica', 16, 'bold'), bg="#edf2f4")
title.pack(pady=10)

# Frame to center content
frame = tk.Frame(root, bg="#edf2f4")
frame.pack(pady=10)

label1 = tk.Label(frame, text="Enter first number :", font=('Helvetica', 12), bg="#edf2f4")
label1.grid(row=0, column=0, sticky='w', pady=5)

entry1 = tk.Entry(frame, font=('Helvetica', 12))
entry1.grid(row=0, column=1, pady=5)

label2 = tk.Label(frame, text="Enter second number :", font=('Helvetica', 12), bg="#edf2f4")
label2.grid(row=1, column=0, sticky='w', pady=5)

entry2 = tk.Entry(frame, font=('Helvetica', 12))
entry2.grid(row=1, column=1, pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#edf2f4")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add", command=add, font=('Helvetica', 12), width=10, bg="#90e0ef")
add_button.grid(row=0, column=0, padx=5)

subtract_button = tk.Button(button_frame, text="Subtract", command=subtract, font=('Helvetica', 12), width=10, bg="#ffafcc")
subtract_button.grid(row=0, column=1, padx=5)

multiply_button = tk.Button(button_frame, text="Multiply", command=multiply, font=('Helvetica', 12), width=10, bg="#ffcc5b")
multiply_button.grid(row=0, column=2, padx=5)

divide_button = tk.Button(button_frame, text="Divide", command=divide, font=('Helvetica', 12), width=10, bg="#9ef79e")
divide_button.grid(row=0, column=3, padx=5)

label_result = tk.Label(root, text="Result", font=('Helvetica', 14), bg="#edf2f4")
label_result.pack(pady=20)

root.mainloop()
