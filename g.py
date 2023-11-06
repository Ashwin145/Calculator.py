from tkinter import *

def press(num):
    current = equation.get()
    equation.set(current + str(num))

def equalpress():
    try:
        current = equation.get()
        result = str(eval(current))
        equation.set(result)
    except:
        equation.set("Error")

def clear():
    equation.set("")

if __name__ == "__main__":
    gui = Tk()
    gui.title("Calculator")
    gui.geometry("300x400")
    gui.configure(bg="lightgray")

    equation = StringVar()

    entry_field = Entry(gui, textvariable=equation, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, justify="right")
    entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        button_frame = Frame(gui, bg="lightgray")
        button_frame.grid(row=row_val, column=col_val, padx=5, pady=5)
        button = Button(button_frame, text=button, font=("Helvetica", 16), height=2, width=5, bd=5, bg="lightblue", activebackground="lightcyan")
        button.pack(fill=BOTH, expand=True)
        if button.cget("text") == '=':
            button.bind("<Button-1>", lambda event: equalpress())
        elif button.cget("text") == 'C':
            button.bind("<Button-1>", lambda event: clear())
        else:
            button.bind("<Button-1>", lambda event, key=button.cget("text"): press(key))
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    gui.mainloop()
