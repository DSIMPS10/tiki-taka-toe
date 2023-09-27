import logging
from pandas import DataFrame

from app import run_footy, create_footy_team_board
from utils.classes import FootyGrid
from scoring import update_guesses_table

##########################################################################################################
### THE TIC TAC TOE GAME ###
##########################################################################################################

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def print_board(board,footy_team_obj: FootyGrid):
    print('          ',footy_team_obj.team_a,'|', footy_team_obj.team_b,'|', footy_team_obj.team_c)
    print(footy_team_obj.team_x, board['7'] + '      |       ' + board['8'] + '      |       ' + board['9'])
    print('          ','---------+---------+----------')
    print(footy_team_obj.team_y, board['4'] + '      |       ' + board['5'] + '      |       ' + board['6'])
    print('          ','---------+---------+----------')
    print(footy_team_obj.team_z, board['1'] + '      |       ' + board['2'] + '      |       '+ board['3'])

def check_winner(count: int, turn: int,footy_team_obj: FootyGrid):
    is_there_a_winner: bool = False
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top             
        is_there_a_winner = True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
        is_there_a_winner = True
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
        is_there_a_winner = True
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
        is_there_a_winner = True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
        is_there_a_winner = True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
        is_there_a_winner = True
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
        is_there_a_winner = True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
        is_there_a_winner = True
    
    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    elif count == 9 and is_there_a_winner == False:
        print("\nGame Over.\n")                
        print("It's a Tie!!")
        #Return true for game over
        return True
    
    if is_there_a_winner:
        print_board(theBoard,footy_team_obj)

        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")

    return is_there_a_winner

def switch_turn(turn: str) -> str:   
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'  
    return turn

def restart_game(restart: str):
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "
        game()

def pass_move(move,turn,pass_dict):
    turn_pass=False
    if move == 'pass':
        turn_pass = True
        if turn == 'X':
            print("Player X has passed")
            pass_dict['pass_player_X'] = True
        if turn == 'O':
            print("Player O has passed")
            pass_dict['pass_player_O']  = True
    return turn_pass, pass_dict
    
def check_move(move):
    try: 
        move = int(move)  
        print(move)
    except ValueError as e:
        print('Please chose an INTEGER value (between 1 and 9)')  
        return False   
    try:
        if move > 9 or move < 1:
            raise ValueError(f'{move} is outside the range 1 to 9. Please chose a new position')
    # except ValueError as e:
    #     print(move, 'is outside the randge 1 to 9. Please chose a new position')
    #     return False
    except Exception as e:
        logging.exception(e)
        return False
    else:
        return True


def game():
    level = input(f'Select your level: [easy, medium, hard]')
    pass_move_dict = {'pass_player_X':False,'pass_player_O':False}
    turn = 'X'
    count = 0
    is_there_a_winner = False   
    footy_team_obj = create_footy_team_board(level)

    while is_there_a_winner == False:
        print_board(theBoard,footy_team_obj)
        print("It's your turn " + turn + ". Choose a location? (type 'pass' if you cannot go)")

        move = input()
        pass_move_passed = pass_move(move,turn,pass_move_dict)[0]
        pass_move_dict = pass_move(move,turn,pass_move_dict)[1]
        if pass_move_passed:
            if pass_move_dict['pass_player_X'] is True and pass_move_dict['pass_player_O'] is True:
                print("Both players have passed, restarting grid.")
                restart_game("y")
            else:
                turn = switch_turn(turn)
                continue

        if check_move(move):      
            move = str(move)
            if theBoard[move] == ' ':
                # theBoard[move] = turn
                # count += 1
                if run_footy(int(move), footy_team_obj):
                    theBoard[move] = turn
                    count += 1
                else:
                    turn = switch_turn(turn)
                    continue
            else:
                print("That place is already filled.\nChoose a location?")
                continue
        else:
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 3:
            is_there_a_winner = check_winner(count, turn, footy_team_obj)
            # if is_there_a_winner:
            #     break
        # Switch player after each go
        turn = switch_turn(turn)
  
    # Optional restart:
    restart = input("Do want to play Again?(y/n)")
    restart_game(restart)

if __name__ == "__main__":
    game()