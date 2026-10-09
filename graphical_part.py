import tkinter as tk
import tkinter.ttk as ttk
from make_password import make_password
from tkinter import messagebox
import pyperclip
window = tk.Tk()
window.iconbitmap("Smile.ico")
window.title("password_maker")
window.geometry("800x300")
mainColor= "#E1FF20"
window.config(background=mainColor)

def generate_password():
    password_length = slider.get()
    has_upper = uppercase_check_var.get()
    has_lower = lowercase_check_var.get()
    has_number = numbers_check_var.get()
    has_symbol = symbols_check_var.get()
    password =make_password(password_length, [has_upper, has_lower, has_number, has_symbol])
    messagebox.showinfo('Your password', password)
    pyperclip.copy(password)


style = ttk.Style()
style.configure("TLabel", background=mainColor, font=('Arial', 15, "bold"))
style.configure("TCheckbutton", background=mainColor, font=('Arial', 15, "bold"))
style.configure("TButton", font=('Arial', 23, "bold"))

descriptionlable = ttk.Label(window, text="Customize your password")
lengthLable = ttk.Label(window, text="password length")
slider = tk.Scale(window, from_=4, to=32, orient="horizontal", background=mainColor)
slider.set(16)

uppercase_check_var = tk.BooleanVar()
lowercase_check_var = tk.BooleanVar()
numbers_check_var = tk.BooleanVar()
symbols_check_var = tk.BooleanVar()

uppercase_check = ttk.Checkbutton(window, text="Uppercase", variable=uppercase_check_var)
lowercase_check = ttk.Checkbutton(window, text="Lowercase", variable=lowercase_check_var)
numbers_check = ttk.Checkbutton(window, text="Numbers", variable=numbers_check_var)
symbols_check = ttk.Checkbutton(window, text="symbols", variable=symbols_check_var)

generat_password = ttk.Button(window, text="Generate password", command=generate_password)


descriptionlable.grid(row=0 ,column=0, sticky="news")
lengthLable.grid(row=1, column=0, sticky="news")
slider.grid(row=1, column=1, columnspan=3, sticky="news")
uppercase_check.grid(row=2, column=0, sticky="news")
lowercase_check.grid(row=2, column=1, sticky="news")
numbers_check.grid(row=2, column=2, sticky="news")
symbols_check.grid(row=2, column=3, sticky="news")   
generat_password.grid(row=3, column=0, columnspan=4, sticky="news")

for i in range(4):
    for j in range(4):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(j, weight=1)



#window.rowconfigure(0, weight=1)
#window.columnconfigure(0, weight=1)

#window.rowconfigure(0, weight=1)
#window.columnconfigure(1, weight=1)

#window.rowconfigure(0, weight=1)
#window.columnconfigure(2, weight=1)

#window.rowconfigure(0, weight=1)
#window.columnconfigure(3, weight=1)


window.mainloop()
