import num2words as n2w
from tkinter import *

def numberstowords():
    try:
        given_num = float(num.get())
        
        # Separate integer and decimal parts
        integer_part = int(given_num)
        decimal_part = abs(given_num - integer_part)
        
        # Convert integer and decimal parts to words
        num_in_word = n2w.num2words(integer_part).capitalize()
        
        if decimal_part > 0:
            decimal_in_word = n2w.num2words(int(decimal_part * 10 ** len(str(decimal_part).split(".")[1])))
            num_in_word += f" point {decimal_in_word}"
        
        display.config(text=str(num_in_word))
    except ValueError:
        display.config(text="Invalid input. Please enter a valid number.")

root = Tk()
root.title('Numbers to Words')
root.geometry('600x350')

num = StringVar()

title = Label(root, text='Number to Words Converter', fg='grey', font=('Arial', 15, 'bold')).place(x=220, y=10)

formats_label = Label(root, text="Formats supported:", fg="green", font=("Arial", 10, 'bold')).place(x=100, y=70)
pos_format_label = Label(root, text="1. Positives", fg="green", font=("Arial", 10, 'bold')).place(x=200, y=90)
neg_format_label = Label(root, text="2. Negatives", fg="green", font=("Arial", 10, 'bold')).place(x=200, y=110)
zero_format_label = Label(root, text="3. Zeros", fg="green", font=("Arial", 10, 'bold')).place(x=200, y=130)
float_format_label = Label(root, text="4. Floating points/decimals/fractions", fg="green", font=("Arial", 10, 'bold')).place(x=200, y=150)

num_entry_label = Label(root, text="Enter a number:", fg="Blue", font=("Arial", 15, 'bold')).place(x=50, y=200)
num_entry = Entry(root, textvariable=num, width=30).place(x=220, y=200)

btn = Button(master=root, text="Calculate", fg="green", font=("Arial", 10, 'bold'), command=numberstowords).place(x=280, y=230)

display = Label(root, text="", fg="black", font=("Arial", 10, 'bold'))
display.place(x=10, y=300)

# Ensure the path to the image file is correct
photo = PhotoImage(file="number.png")
root.iconphoto(False, photo)

root.mainloop()
