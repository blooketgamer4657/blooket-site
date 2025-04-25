import tkinter as tk
from tkinter import messagebox
import webbrowser

# --- Configuration ---
CORRECT_PASSWORD = "cocomelon"

# --- Functions ---
def check_password():
    entered = password_entry.get()
    if entered == CORRECT_PASSWORD:
        open_button.pack(pady=10)
        messagebox.showinfo("Access Granted", "Password is correct!")
    else:
        messagebox.showerror("Access Denied", "Incorrect password.")

def open_google():
    webbrowser.open("https://githubman6996.github.io/05konz-blooket-site/")

# --- GUI Setup ---
root = tk.Tk()
root.title("Secure Button Access")
root.geometry("300x200")

label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack()

submit_button = tk.Button(root, text="Submit", command=check_password)
submit_button.pack(pady=5)

open_button = tk.Button(root, text="Go to Google", command=open_google)
# Don't pack it yet — only after correct password!

root.mainloop()
