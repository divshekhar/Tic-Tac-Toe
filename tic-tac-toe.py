
# from IPython.display import clear_output
import os

def welcome():
    clear_screen()
    print("\n*****************************************************")
    print("\n\tWelcome to the Tic-Tac-Toe Game")
    print("\t","=>created by Divyanshu Shekhar\n")
    print("\n*****************************************************\n")
    dummy_board()
    print("\nThis is the Tic-Tac-Toe Board showing the position ")
    print("of each boxes where either 'X' or 'O' will be placed.\n")
    print("\nEnter 0 in any input field to exit\n")


def exitGame(ch):
    if ch == '0':
        exit()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def dummy_board():


    print(f"   1 | 2 | 3 ")
    print("  ---|---|---")
    print(f"   4 | 5 | 6 ")
    print("  ---|---|---")
    print(f"   7 | 8 | 9 \n")



def display_board(board):

    print(f"   {board['1']} | {board['2']} | {board['3']}")
    print("  ---|---|---")
    print(f"   {board['4']} | {board['5']} | {board['6']}")
    print("  ---|---|---")
    print(f"   {board['7']} | {board['8']} | {board['9']}")


def valueCheck(chPlayer,board,key,p,ct):
    if board[key] == ' ':
        board[key] = chPlayer[p]
        ct += 1
    return ct




def winner(p1,p2):
    winCon = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
    flag = 0
    for el in winCon:
        if set(el).difference(set(el).intersection(set(p1))) == set():
            flag = 1
            break
        elif set(el).difference(set(el).intersection(set(p2))) == set():
            flag = 2
            break
    return flag






def updateValues(p1,p2,pos,ap):
    if pos not in p1 and pos not in p2:

        if ap == 'player1':
            p1.append(pos)
        else:
            p2.append(pos)
    




def swipeActivePlayer(activeplayer):
    if activeplayer == '1':
        activeplayer = '2'
    elif activeplayer == '2':
        activeplayer = '1'
    return activeplayer


def swipeValues(chPlayer):
    temp = chPlayer['player1']
    chPlayer['player1'] = chPlayer['player2']
    chPlayer['player2'] = temp


def makeChoice(cplayer,player,choice):
    if player == '1' and choice.casefold() == 'o':
        swipeValues(cplayer)
    elif player == '2' and choice.casefold() == 'x':
        swipeValues(cplayer)




def playGame(chplayer,board,choice,activeplayer):

    player1, player2 = [], []
    won = -1
    ap = activeplayer
    clear_screen()
    makeChoice(chplayer,activeplayer,choice)
    
    counter = 1
    while counter <= 9:
        
        print("Choice of Both the players are:\n")
        for a in chplayer:
            print(f"{a} => {chplayer[a]}")
        print("Let's Play the Game Now!!\n")
        
        dummy_board()
        print("********************\n")
        display_board(board)
        p = 'player'+ap
        print()
        print(f"Position of Player-1 {player1}\n")
        print(f"Position of Player-2 {player2}\n")
        

        print(f"--->{'player-'+ap}\n")
        ch = input(f"Enter the Position: --> ")
        
        ct = valueCheck(chplayer,board,ch,p,counter)
        clear_screen()
        if not ct == counter:
            ap = swipeActivePlayer(ap)
        if board[ch] == ' ':
            print(f"\nSorry, This position is already Occupied with {board[ch]}")
            print("\nEnter New Position\n")
        
        updateValues(player1,player2,ch,p)
        
        
        won = winner(player1,player2)
        if won == 1:
            print()
            display_board(board)
            print("\n*****************************************************")
            print("\n\tPlayer 1 ===========> WINNER !!!!\n\n")
            print("*****************************************************\n")
            break
        elif won == 2:
            print()
            display_board(board)
            print("\n*****************************************************")
            print("\n\tPlayer 2 ===========> WINNER !!!!\n\n")
            print("*****************************************************\n")
            break

        
        
        counter = ct

    if won == 0:
        print()
        print("\n*****************************************************")
        print("\n\t\tGame Tied !!!!\n\n")
        print("*****************************************************\n")
        
        
        
        


def startPlay():
    wel = input("Enter 'play' to Start Playing the Game-")
    exitGame(wel)
    while wel.casefold() == 'play':


        board={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
        choice_player = {'player1':'X','player2':'O'}


        wel = 'notPlaying'
        clear_screen()
        print("This is a Two Player Game.\n")
        print("You are PLAYER 1/2 ?")
        player = input("------> ")
        exitGame(player)
        print()
        assert int(player) == 2 or int(player) == 1


        print("Do you Want 'X' or 'O'")
        choice = input("------> ")
        print()
        exitGame(choice)
        assert (choice == 'X' or choice == 'x') or (choice == 'o' or choice == 'O')


        playGame(choice_player,board,choice,player)



        print("Game Over. Do you want to play once again.\n")
        ch = input("Enter y/n ---> ")
        if ch == 'y' or ch == ' Y':
            wel = 'play'
        else:
            wel = 'notPlaying'
        clear_screen()
    else:
        print("COME BACK SOON :)")
        





        
        
        




def main():
    welcome()
    startPlay()



if __name__ == '__main__':
    main()