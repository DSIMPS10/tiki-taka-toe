from tkinter import *
from tkinter import messagebox
# from tkmacosx import Button

root = Tk()
root.title('Tika-taka-toe')

clicked = True
count = 0

def b_click(b):
    global clicked, count
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        b['bg'] = 'yellow'
        clicked = False
        count += 1 
        check_winner()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        b['bg'] = 'yellow'
        clicked = True
        count += 1 
        check_winner()
    else: 
        messagebox.showerror('Tika-taka-tow', 'This location is already taken.\n Pick another location.')

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

    
def check_winner():
    global winner
    if b1['text'] == b2['text'] == b3['text'] != ' ':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b4['text'] == b5['text'] == b6['text'] != ' ':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b7['text'] == b8['text'] == b9['text'] != ' ':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b1['text'] == b4['text'] == b7['text'] != ' ':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b2['text'] == b5['text'] == b8['text'] != ' ':
        b2.config(bg="green")
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b3['text'] == b6['text'] == b9['text'] != ' ':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b1['text'] == b5['text'] == b9['text'] != ' ':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    elif b3['text'] == b5['text'] == b7['text'] != ' ':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        messagebox.showinfo('Tika-taka-toe', 'There is a winner!')
        disable_all_buttons()
    
    if count == 9 and winner == False:
        messagebox.showinfo('Tika-taka-toe', 'The game is a draw, it is a tie.')


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked,count
    clicked = True
    count = 0
    
    b1 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='red', command=lambda: b_click(b1))
    b2 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='red', command=lambda: b_click(b2))
    b3 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='red', command=lambda: b_click(b3))

    b4 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b4))
    b5 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b5))
    b6 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b6))

    b7 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b7))
    b8 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b8))
    b9 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b9))

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

menu = Menu(root)
root.config(menu=menu)

options_menu = Menu(menu, tearoff=True)
menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Reset game', command=lambda: reset())

reset() 

root.mainloop()