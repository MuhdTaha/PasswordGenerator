import tkinter as tk
from tkinter import messagebox
import random

app = tk.Tk()
app.title("Password Generator")
app.geometry("1000x600")

label_length = tk.Label(app, text="Password Length:")
label_length.pack(pady=10)

entry_length = tk.Entry(app)
entry_length.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(app, textvariable=password_var)
password_label.pack(pady=20)

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
            return

        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
        password = "".join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

app.mainloop()
