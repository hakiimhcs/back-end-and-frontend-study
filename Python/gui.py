from tkinter import Tk, Label, Entry, Button
import tkinter.messagebox as messagebox

window = Tk()
window.configure(bg="#417287")
window.title('graphical user interface')
window.geometry("500x600")

heading = Label(window, text="Login", bg="lightblue", fg="white", font=("Consolas", 20, "bold"))
heading.pack(pady=10)

username_label = Label(window, text="Username:", bg="#417287", fg="white", font=("Consolas", 12))
username_label.pack(pady=(10, 0))
username_txt = Entry(window)
username_txt.pack()

password_label = Label(window, text="Password:", bg="#417287", fg="white", font=("Consolas", 12))
password_label.pack(pady=(10, 0))
password_txt = Entry(window, show="*")
password_txt.pack()

def show_message():
    name = username_txt.get()
    passw = password_txt.get()
    if not name or not passw:
        messagebox.showwarning("Missing", "Please enter both username and password.")
        return
    messagebox.showinfo("Credentials", f"Username: {name}\nPassword: {passw}")

login_btn = Button(window, text="Login", command=show_message)
login_btn.pack(pady=20)
