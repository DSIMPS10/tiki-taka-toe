import logging
from app import run_footy, create_footy_team_board

##########################################################################################################
### THE TIC TAC TOE GAME ###
##########################################################################################################

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def check_winner(count, turn):
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
        printBoard(theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")

    return is_there_a_winner

def switch_turn(turn):   
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'  
    return turn

def restart_game(restart):
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "
        game()
    
def check_move(move):
    try: 
        move = int(move)  
    except ValueError as e:
        print('Please chose an INTEGER value (between 1 and 9)')  
        return False   

    try:
        if move > 9 or move < 1:
            raise ValueError(move)
    except ValueError as e:
        print(move, 'is outside the randge 1 to 9. Please chose a new position')
        return False
    except Exception as e:
        logging.exception(e)
        return False
    else:
        return True


def game():
    turn = 'X'
    count = 0
    is_there_a_winner = False
    
    footy_team_board_df = create_footy_team_board()

    while is_there_a_winner == False:
        printBoard(theBoard)
        print("It's your turn " + turn + ". Choose a location?")

        move = input()
        if check_move(move):      
            move = str(move)
            if theBoard[move] == ' ':
                # theBoard[move] = turn
                # count += 1
                if run_footy(int(move)):
                    theBoard[move] = turn
                    count += 1
                else:
                    continue
            else:
                print("That place is already filled.\nChoose a location?")
                continue
        else:
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            is_there_a_winner = check_winner(count, turn)
            # if is_there_a_winner:
            #     break
        # Switch player after each go
        turn = switch_turn(turn)
  
    # Optional restart:
    restart = input("Do want to play Again?(y/n)")
    restart_game(restart)

if __name__ == "__main__":
    game()