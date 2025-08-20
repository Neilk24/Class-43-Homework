from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Password Strength Checker')
root.geometry('1000x1000')
color='default'

def check(pwd):
    if len(pwd) <= 5:
        color = 'red'
    elif 6<=len(pwd)<=8:
        color = 'yellow'
    elif 8<len(pwd)<=12:
        color = 'light_green'
    elif len(pwd)>12:
        color = 'dark_green'

    return color

def topwin():
    top = Toplevel()
    top.title('Password Check Result')
    top.geometry('500x500')

    color = check(pwd=entry.get())

    label1 = Label(top, text='The result of your check is: ')
    label1.place(x=10, y=20)

    if color == 'red':
        label2 = Label(top, text = 'weak', fg='black', bg='red')
        label2.place(x=160, y=20)

    elif color == 'yellow':
        label2 = Label(top, text = 'medium', fg='black', bg='yellow')
        label2.place(x=160, y=20)

    elif color == 'light_green':
        label2 = Label(top, text = 'strong', fg='black', bg='light green')
        label2.place(x=160, y=20)

    elif color == 'dark_green':
        label2 = Label(top, text = 'very strong', fg='black', bg='dark green')
        label2.place(x=160, y=20)

    

label = Label(root, text='Type your password:')
entry = Entry()

def message():
    msgbox = messagebox.showinfo('Alert!', 'Checking...')
    if msgbox == 'ok':
        topwin()

button = Button(text='Submit!', command=message)

label.place(x=50, y=100)
entry.place(x=169, y=100)
button.place(x=100, y=150)

root.mainloop()