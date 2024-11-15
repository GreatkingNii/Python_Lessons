import tkinter as tk
from tkinter import messagebox

def login():

    username= user.get()
    password= passw.get()

    if username in ('great','success'): 
        if password =='ttyl123':
            messagebox.showinfo('Login successful', 'Permission granted')
            root.destroy()
          
    
    else:
        messagebox.showerror('Invalid credentials', 'Login failed')
        retries[0] -= 1
        retry_label.config (text = f'Retries remaining: {retries[0]}')

        if retries [0] == 0:
            messagebox.showerror('Access denied')
            root.destroy()

root =tk.Tk()
root.title('Login')
root.geometry('300x200')

retries = [3]

username_label = tk.Label(root, text = 'Username')
username_label.pack(pady=5)
user = tk.Entry(root)
user.pack(pady=5)

password_label = tk.Label(root, text='Password')
password_label.pack(pady= 5)
passw=tk.Entry(root, show='*')
passw.pack(pady=5)

retry_label=tk.Label(root, text=f'Your remaining retries are: {retries[0]}')
retry_label.pack(pady=5)

login_btn = tk.Button(root, text='Login', command=login)
login_btn.pack(pady=10)

root.mainloop()

