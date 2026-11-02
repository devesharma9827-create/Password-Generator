import random
import string
from tkinter import *

def generate():
    length = int(entry.get())
    if length > 10:
        result.config(text="Length cannot exceed 10")
        return
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password = password + random.choice(all_characters)
    result.config(text=password)

window = Tk()
window.title("Password Generator")
window.geometry("300x200")

Label(window, text="Enter password length (max 10):").pack(pady=10)
entry = Entry(window)
entry.pack()
Button(window, text="Generate", command=generate).pack(pady=10)
result = Label(window, text="", font=("Arial", 14))
result.pack()

window.mainloop()