import tkinter as tk

def button_click(item):
    """Add button's text to the entry field."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + item)

def clear():
    """Clear the entry field."""
    entry.delete(0, tk.END)

def calculate():
    """Evaluate the expression in the entry field."""
    try:
        result = eval(entry.get())  # eval parses the expression safely here
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Stunning Calculator")
root.geometry("400x500")
root.config(bg="#edf2f4")

entry = tk.Entry(root, font=('Helvetica', 24), borderwidth=5, relief='solid')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Define button texts in a grid format
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_vals = 1
col_vals = 0
for item in buttons:
    if item == "=":
        cmd = calculate
    elif item == "C":
        cmd = clear
    else:
        cmd = lambda x=item: button_click(x)

    button = tk.Button(root, text=item, font=('Helvetica', 20), width=4, height=2, 
                       command=cmd, bg="#ffcc5b")
    button.grid(row=row_vals, column=col_vals, padx=5, pady=5)

    col_vals += 1
    if col_vals > 3:
        col_vals = 0
        row_vals += 1

root.mainloop()
