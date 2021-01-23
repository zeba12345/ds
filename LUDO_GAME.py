print("DICE ROLL GAME")
import random

def main():
    player1=0
    player1wins=0
    player2=0
    player2wins=0
    Rounds=1
    
    
    while (Rounds!=10):
        print("Round "+str(Rounds))
        player1=Dice_Roll()
        player2=Dice_Roll()
        print("Player 1 Roll: "+ str(player1))
        print("Player 2 Roll: "+ str(player2))
        
        if(player1==player2):
            player1wins=player1wins + 1
            print("Draw !!")
        elif(player1>player2):
            player2wins=player2wins + 1
            print("Player1 wins!\n")
        else:
            print("Player2 wins!\n")
            
        Rounds=Rounds+1
        
    if(player1wins==player2wins):
        print("Draw !")
    elif(player1wins>player2wins):
        print("PLAYER 1 wins! - Rounds won: "+str(player1wins))
    else:
        print("PLAYER 2 wins! - Rounds won: "+str(player2wins))
        
        
def Dice_Roll():
    diceRoll=random.randint(1, 6)
    return diceRoll
    
main()