import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from myage import *
root=tk.Tk()

root.title('Age calculator')
root.geometry('400x100')
root.resizable(False, False)

frame = ttk.Frame(root)
options = {'padx':5, 'pady':5}
age_label = ttk.Label(root, text ='Enter your year of birth')
age_label.grid (column=0,row=0, **options)

age= tk.StringVar()
age_entry= ttk.Entry(root, textvariable=age)
age_entry.grid(column=1, row=0, **options)
age_entry.focus()

def convert_button():
    try:
        year=int(age.get())
        dob = age
        result = f'you are {dob} years old'
        result_label.config
    
    except ValueError as error:
        showerror(title='Error', message=error)

btn =tk.Button(root, text='Convert')
btn.grid(column=2, row=0, **options)
btn.configure(command=convert_button)

result_label = tk.Label(root)
result_label.grid(columnspan=2, row=1, **options)

root.mainloop ()

