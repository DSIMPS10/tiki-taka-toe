from tkinter import *
from tkinter import messagebox
# from tkmacosx import Button

root = Tk()
root.title('Tika-taka-toe')

clicked = True
count = 0

def b_click(b: Button, number: int, teams: Label):
    global clicked, count

    if number == 1: 
        teams['text'] = 'Team A & Team X'
    elif number == 2: 
        teams['text'] = 'Team B & Team X'
    elif number == 3: 
        teams['text'] = 'Team C & Team X'
    elif number == 4: 
        teams['text'] = 'Team A & Team Y'
    elif number == 5: 
        teams['text'] = 'Team B & Team Y'
    elif number == 6: 
        teams['text'] = 'Team C & Team Y'  
    elif number == 7: 
        teams['text'] = 'Team A & Team Z'
    elif number == 8: 
        teams['text'] = 'Team B & Team Z'
    elif number == 9: 
        teams['text'] = 'Team C & Team Z'   
        
        
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

def submit_choice(player: str, player_submitted: Label):
    player_submitted['text'] = player

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked,count
    clicked = True
    count = 0
    
    b1 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='red', command=lambda: b_click(b1, 1, teams))
    b2 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='red', command=lambda: b_click(b2, 2, teams))
    b3 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='red', command=lambda: b_click(b3, 3, teams))

    b4 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b4, 4, teams))
    b5 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b5, 5, teams))
    b6 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b6, 6, teams))

    b7 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b7, 7, teams))
    b8 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b8, 8, teams))
    b9 = Button(root, text=' ', font=('Helvetica',20), height=3, width=6, bg='white', command=lambda: b_click(b9, 9, teams))
    
    current_row = 0
    title = Label(text='Tika Taka Toe',font=('Helvetica',20))
    title.grid(row=current_row, column=0, columnspan=4)   
    team_a_label = Label(text='Team A')
    team_b_label = Label(text='Team B')
    team_c_label = Label(text='Team C')
    team_x_label = Label(text='Team X')
    team_y_label = Label(text='Team Y')
    team_z_label = Label(text='Team Z')

    current_row +=1
    team_a_label.grid(row=current_row, column=1)
    team_b_label.grid(row=current_row, column=2)
    team_c_label.grid(row=current_row, column=3)
    
    current_row +=1
    team_x_label.grid(row=current_row, column=0)
    b1.grid(row=current_row, column=1)
    b2.grid(row=current_row, column=2)
    b3.grid(row=current_row, column=3)
    
    current_row +=1
    team_y_label.grid(row=current_row, column=0)
    b4.grid(row=current_row, column=1)
    b5.grid(row=current_row, column=2)
    b6.grid(row=current_row, column=3)
    
    current_row +=1
    team_z_label.grid(row=current_row, column=0)
    b7.grid(row=current_row, column=1)
    b8.grid(row=current_row, column=2)
    b9.grid(row=current_row, column=3)
    
    current_row +=2
    teams_selected = Label(text='Teams selected: ',font=('Helvetica',15))
    teams_selected.grid(row=current_row, column=0, columnspan=2)
    
    team_names = 'Select a square...'
    teams = Label(text=team_names,font=('Helvetica',15))
    teams.grid(row=current_row, column=2, columnspan=2)
    
    current_row +=1
    player_guess_label = Label(text='Guess: ',font=('Helvetica',15))
    player_guess_label.grid(row=current_row, column=1, columnspan=1)
    
    player_name = 'Raheem Sterling'
    player = Entry(root)
    player.grid(row=current_row, column=2, columnspan=2)
    
    submit_guess = Button(root, text='Submit', font=('Helvetica',10), height=3, width=6, bg='white', command=lambda: submit_choice(player))
    submit_guess.grid(row=current_row, column=4)
    
    current_row +=1
    player_submitted_label = Label(text='Player submitted: ',font=('Helvetica',15))
    player_submitted_label.grid(row=current_row, column=1, columnspan=1)
    player_submitted = Label(text=player,font=('Helvetica',15))
    player_submitted.grid(row=current_row, column=3, columnspan=1)
    

menu = Menu(root) 
root.config(menu=menu)

options_menu = Menu(menu, tearoff=True)
menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Reset game', command=reset)

reset() 

root.mainloop()