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
root.geometry("400x250")

label1 = tk.Label(root, text="Enter first number")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

label_result = tk.Label(root, text="Result")
label_result.pack()

root.mainloop()
