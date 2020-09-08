#Nabil Yasser
#Python3~

from random import *    #Importing all the elements from the module random                                                                                                   
#                                                                                                                                              
import sys#                                                                                                                                    
try: color = sys.stdout.shell                                          #Importing sys                                                              
except AttributeError: raise RuntimeError("Use IDLE")                  #to color our algorithm                                                      
try:                                                                   #colorama doesn't work                                                        
    shell = sys.stdout.shell                                           #so I had to rely                                                              
except AttributeError:                                                 #on sys instead                                                                  
    raise RuntimeError("you must run this program in IDLE")            #pretty good difference but it still works
#
def RESTART():#
    print("\n")#
    shell.write("                                   TO -- ENJOY -- THE -- GAME -- PLAY -- IN -- FULLSCREEN\n","COMMENT")#
    shell.write("                             <From now on, please press Enter every time you want to continue>","KEYWORD")#
    Y = input("")#
    print("                                                   Welcolme to my Game!\n")#
    print("                               First, write your names. Second, know the rules. Last, Enjoy.\n")#
    player1 = input("                       Player 1's name(5 Characteres): ")#
    while player1.isalpha() == False or len(player1)> 5 or len(player1)<5:                                #Verifies if all the
        shell.write("                       Just letters please! And obviously 5 characters.\n","hit")                #Conditions are correct
        player1 = input("                       Player 1's name(5 Characteres): ")                        #Which are:
    if player1.isalpha() == True and len(player1) == 5:                                                   #_5 Characters
        player2 = input("                       Player 2's name(5 Characteres): ")                        #_no symbols or numbers
        while player2.isalpha() == False or len(player2)> 5 or len(player2)<5:                            #For each player.                                                     
            shell.write("                       Just letters please! And obviously 5 characters.\n","hit")
            player2 = input("                       Player 2's name(5 Characteres): ")
        if player2.isalpha() == True and len(player2) == 5:
            shell.write("\n                       Rules:\n\n                             15 boxes are in this board\n                             Each box have a special effect\n                             Some give you money, some make you lose it, etc.\n                             For this game the dices are 1-2-3 Dices\n                             The goal is to finish the game with more money than your opponent\n\n","COMMENT")
            print("                       Anyway, You will continue to roll the dices until the number of rounds becomes 0")
            Y = input("")
            print("                       Are you interested about every box and its effect on the player?\n                       Type Y if you want to know more about each box or Enter if you want to pass!")
            effect = input("                       - ")
            if effect == "Y" or effect == "y":
                print("")
                shell.write("\nBox 1:  Gain 200 $.\n","hit")
                shell.write("Box 2:  Gain 100 $ Times the number of time players landed on it.\n","hit")
                shell.write("Box 3:  ReRoll.\n","hit")
                shell.write("Box 4:  The player who lands select a value for a variable, if it isn't set before. \n        When a player re-land on the box, he guesses the variable's value, if he gets it correct he gain 400 $.\n","hit")
                shell.write("Box 5:  Your money will be divided by the number you got in your Dices.\n","hit")
                shell.write("Box 6:  Lose 200 $\n","hit")
                shell.write("Box 7:  You will be protected from the next lost of money.\n","hit")
                shell.write("Box 8:  Gamble X, for a prize X/ 0 < X < 6*X\n","hit")
                shell.write("Box 9:  Every time you land on Box 10/11 you pay 10% of your money$, unless you have landed in Box 9 before.\n        However, if you land on it you will collect all the money paid before.\n","hit")
                shell.write("Box 10: Doubles your actual money.\n","hit")
                shell.write("Box 11: You reroll the dice, and if it shows '2' you will change your money with your opponent.\n","hit")
                shell.write("Box 12: You guess a random number from 1 to 30, if you get it right you gain 600$ and the number changes.\n        Else the random number won't change and you don't gain anything.\n","hit")
                shell.write("Box 13: Sends the player to the next boxes (random from 1 to 11). The player won't get its effect.\n","hit")
                shell.write("Box 14: Sends the player to the first box without getting its effect!\n","hit")
                shell.write("Box 15: You gamble 100 Money and roll the dices, if you get '1', you gain 600 Money.\n\n","hit")
                print("Back to the game!\n")
            else:
                print("As you like\n")
            Y = input("")
#Variables: Turn (The number of round the players will play)- case1/2(The position of every player)- p1/2money(Players money)-
#barrier1/2 (protection for the loss of money)- rand(decides if the players first landed on box 12)- tax(the ammount payed from the players while passing through box 9)
#antitax1/2 (when the player landed on the jackpot, he won't pay if he lands in box 10/11)- T(Times players landed on the Box 2)- landed(verifies if players already landed
#in the Box 4)- possibilities(the numbers you can choose to select the time you'll spend in the game)- turn(The number of rounds the players will play)                      
            turn = 0
            possibilities = [int(1), int(2), int(3)]
            case1 = 0
            case2 = 0
            p1money = 100
            p2money = 100
            barrier1 = 0
            barrier2 = 0
            rand = 0
            tax = 0
            antitax1 = 0
            antitax2 = 0
            T = 1
            landed = 0
#Definitions of the functions that will help each other to print the board for every player's turn.
            def Print1(x):
                Line1= ["||    1    ","    2    ","    3    ","    4    ","    5    ","    6    ","    7    ","    8    ","    9    ","    10   ","    11   ","    12   ","    13   ","    14   ","    15   ||"]
                Line2= ["","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ",""]
                Line4= ["","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ",""]
                Line3= ["||         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ||"]
                print("="*167)
                print("||".join(Line1))
                print("="*167)
                Line2[x+1] = "  "+player1+"  "
                print("||".join(Line2))

            def Print2(x):
                Line1= ["||    1    ","    2    ","    3    ","    4    ","    5    ","    6    ","    7    ","    8    ","    9    ","    10   ","    11   ","    12   ","    13   ","    14   ","    15   ||"]
                Line2= ["","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ",""]
                Line4= ["","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ",""]
                Line3= ["||         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ","         ||"]
                Line4[x+1] = "  "+player2+"  "
                print("||".join(Line4))
                print("||".join(Line3))
                print("||".join(Line3))
                print("||".join(Line3))
                print("||".join(Line3))
                print("||".join(Line3))
                print("||".join(Line3))
                print("||".join(Line3))

            def PrintBoard():
                if case1 == 1:
                    Print1(0)
                elif case1 == 2:
                    Print1(1)
                elif case1 == 3:
                    Print1(2)
                elif case1 == 4:
                    Print1(3)
                elif case1 == 5:
                    Print1(4)
                elif case1 == 6:
                    Print1(5)
                elif case1 == 7:
                    Print1(6)
                elif case1 == 8:
                    Print1(7)
                elif case1 == 9:
                    Print1(8)
                elif case1 == 10:
                    Print1(9)
                elif case1 == 11:
                    Print1(10)
                elif case1 == 12:
                    Print1(11)
                elif case1 == 13:
                    Print1(12)
                elif case1 == 14:
                    Print1(13)
                elif case1 == 15:
                    Print1(14)

                if case2 == 1:
                    Print2(0)
                elif case2 == 2:
                    Print2(1)
                elif case2 == 3:
                    Print2(2)
                elif case2 == 4:
                    Print2(3)
                elif case2 == 5:
                    Print2(4)
                elif case2 == 6:
                    Print2(5)
                elif case2 == 7:
                    Print2(6)
                elif case2 == 8:
                    Print2(7)
                elif case2 == 9:
                    Print2(8)
                elif case2 == 10:
                    Print2(9)
                elif case2 == 11:
                    Print2(10)
                elif case2 == 12:
                    Print2(11)
                elif case2 == 13:
                    Print2(12)
                elif case2 == 14:
                    Print2(13)
                elif case2 == 15:
                    Print2(14)
                print("\n")
            def PrintBox(x):
                if x == 1:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 1:      + 200 $                                                                                          ||")
                    print("       ===============================================================================================================================")
                if x == 2:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 2:      + 100 $ * Times player landed there                                                              ||")
                    print("       ===============================================================================================================================")
                if x == 3:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 3:      ReRoll                                                                                           ||")
                    print("       ===============================================================================================================================")
                if x == 4:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 4:      Chance!                                                                                          ||")
                    print("       ===============================================================================================================================")
                if x == 5:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 5:      Your Money will be divided by how much you will get in you Roll                                  ||")
                    print("       ===============================================================================================================================")
                if x == 6:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 6:      - 200 $                                                                                          ||")
                    print("       ===============================================================================================================================")
                if x == 7:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 7:      Barrier                                                                                          ||")
                    print("       ===============================================================================================================================")
                if x == 8:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 8:      Kakegurui (Japanese)                                                                             ||")
                    print("       ===============================================================================================================================")
                if x == 9:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 9:      Jackpot $$$                                                                                      ||")
                    print("       ===============================================================================================================================")
                if x == 10:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 10:     Doubles Your Money!                                                                              ||")
                    print("       ===============================================================================================================================")
                if x == 11:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 11:     Change your money with your opponent (If you'll get 2 in your Roll)                              ||")
                    print("       ===============================================================================================================================")
                if x == 12:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 12:     Guess the number to Win A MILLION (1000 $)                                                       ||")
                    print("       ===============================================================================================================================")
                if x == 13:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 13:     Coup de BURST                                                                                    ||")
                    print("       ===============================================================================================================================")
                if x == 14:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 14:     Back to the START                                                                                ||")
                    print("       ===============================================================================================================================")
                if x == 15:
                    print("       ===============================================================================================================================")
                    print("       ||              BOX 15:     Risk 100$ to win 600$                                                                            ||")
                    print("       ===============================================================================================================================")
#The end of the definition of the functions                                                                                                                                     E
            shell.write("                       You both start with 100 of money! Try to make it huge.\n","KEYWORD")
            Y = input("")
            print("How much do you want to play?")
            print("Choose between:    1     -    2     -  3\n               A little     Normal    Long")
            Y = input("Choose the number: ")
            while Y.isdigit() == False or int(Y) not in possibilities:
                print("Please choose a number from the choices")
                Y = input("Choose the number: ")
            if int(Y) == 1:
                turn = 25
            elif int(Y) == 2:
                turn = 35
            elif int(Y) == 3:
                turn = 45

            while turn != 0:
                if p1money <0:  # Double (Already verified when the player land on the box)                                                                                     M
                    p1money = 0 # Verification
                if p2money <0:  # Of the players'
                    p2money = 0 # Money
                print("   -------------------------------------------------------",player1,"'s Turn!-------------------------------------------------------")#Announces the
                Y = input("                                                  Press Enter to Roll Dices")#                                                     1st Player turn
                dice1 = randint(1, 3)
                case1 += dice1
                if case1 > 15:                                        #Positions correctly the player's position
                    case1 -= 15                                       #(Don't go above the board's boundaries)
                print("                       Your Dice: ",dice1)
                if case1 == 1:# The player lands on Box 1
                    PrintBoard()
                    PrintBox(1)
                    print(player1,"actual money:",p1money)
                    p1money += 200
                    print("\nYou got 200$")
                    print(player1,"now have",p1money)

                elif case1 == 2:# The player lands on Box 2
                    PrintBoard()
                    PrintBox(2)
                    print(player1,"actual money:",p1money)
                    print("Players have landed on this box",T,"times before")
                    p1money += 100 * int(T)
                    T += 1
                    print(player1,"'s money became",p1money)

                elif case1 == 3:#The player lands on Box 3
                    PrintBoard()
                    PrintBox(3)
                    print(player1,"actual money:",p1money)
                    Y = input("                                             Press Enter to ReRoll Dices")
                    dice1 = randint(1, 3)
                    case1 += dice1#          When the player ReRolls
                    if case1 > 15:#          these commands helps him to get the effect of each
                        case1 -= 15#         box he lands on

###################################################           ReRoll              #############################################################                                 
                    if case1 == 4:#The player lands on Box 4 (ReRoll)
                        PrintBoard()
                        PrintBox(4)
                        print(player1,"actual money:",p1money)
                        if landed == 0:
                            print("Choose a value for the Number 'K' ( From 0 to 20) : ")
                            K = input("What value do you assign?> ")
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            while K.isdigit() == False or int(K) not in range(21):
                                print("A Number[0-20] please")
                                K = input("A value to K ( From 0 to 20 )> ")
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            landed = 1
                        elif landed != 0:
                            print("What is the value of the Number? From 0 to 20")
                            Kguess = input("K = ")
                            while Kguess.isdigit() == False or int(K) not in range(21):
                                print("The value of your guess must be a Number! From 0 to 20")
                                Kguess = input("K = ")
                            if int(Kguess) == int(K):
                                print("You won!!!")
                                p1money +=400
                                print(player1,"'s money became:",p1money)
                                landed = 0
                            else:
                                print("Maybe next time")

                    elif case1 == 5:#The player lands on Box 5 (ReRoll)
                        PrintBoard()
                        PrintBox(5)
                        print(player1,"actual money:",p1money)
                        p1money = int(p1money/dice1)
                        print(player1,"'s money is now",p1money)

                    elif case1 == 6:#The player lands on Box 6 (ReRoll)
                        PrintBoard()
                        PrintBox(6)
                        print(player1,"actual money:",p1money)
                        if barrier1>0:
                            barrier1 -=1
                            print("You were saved from your barrier, you won't lose 200 $")
                            print("Barrier left:",barrier2)
                        else:
                            p1money -= 200
                            if p1money <0:
                                p1money = 0
                            print("\nYou lost 200$")
                            print(player1,"now have",p1money)
###################################################           ReRoll              #############################################################                                 E

                elif case1 == 4:#The player lands on Box 4
                    PrintBoard()
                    PrintBox(4)
                    print(player1,"actual money:",p1money)
                    if landed == 0:
                        print("Choose a value for the Number 'K' ( From 0 to 20) : ")
                        K = input("What value do you assign?> ")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        while K.isdigit() == False or int(K) not in range(21):
                            print("A Number[0-20] please")
                            K = input("A value to K ( From 0 to 20 )> ")
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        landed = 1
                    elif landed != 0:
                        print("What is the value of the Number? From 0 to 20")
                        Kguess = input("K = ")
                        while Kguess.isdigit() == False or int(K) not in range(21):
                            print("The value of you guess must be a Number! From 0 to 20")
                            Kguess = input("K = ")
                        if int(Kguess) == int(K):
                            print("You won!!!")
                            p1money +=400
                            print(player1,"'s money became:",p1money)
                            landed = 0
                        else:
                            print("Maybe next time")

                elif case1 == 5:#The player lands on Box 5                                                                                                                      R
                    PrintBoard()
                    PrintBox(5)
                    print(player1,"actual money:",p1money)
                    p1money = int(p1money/dice1)
                    print(player1,"'s money is now",p1money)

                elif case1 == 6:#The player lands on Box 6
                    PrintBoard()
                    PrintBox(6)
                    print(player1,"actual money:",p1money)
                    if barrier1>0:
                        barrier1 -=1
                        print("You were saved from your barrier, you won't lose 200 $")
                        print("Barrier left:",barrier2)
                    else:
                        p1money -= 200
                        if p1money <0:
                            p1money = 0
                        print("\nYou lost 200$")
                        print(player1,"now have",p1money)

                elif case1 == 7:#The player lands on Box 7
                    PrintBoard()
                    PrintBox(7)
                    print(player1,"actual money:",p1money)
                    barrier1 += 1
                    print("You are now protected from the",barrier1,"next lost of money")

                elif case1 == 8:#The player lands on Box 8
                    PrintBoard()
                    PrintBox(8)
                    print(player1,"actual money:",p1money)
                    print("Do you want to Gamble !?")
                    Y = input("How much?>  ")
                    while Y.isdigit() == False or p1money < int(Y):
                        print("Write a NUMBER that you can afford please!")
                        Y = input("Let me repeat, how much?>  ")
                    else:
                        p1money -= int(Y)
                        print(player1,"'s money became",p1money)
                        kakegurui = int(Y) * randint(-1,6)
                        newp1 = int(p1money) + int(kakegurui)
                        p1money = newp1
                        if p1money < 0:
                            p1money = 0
                        print(kakegurui,"will be added to your money!")
                        print(player1,"'s money became:",p1money)

                elif case1 == 9:#The player lands on Box 9                                                                                                                      My
                    PrintBoard()
                    PrintBox(9)
                    print(player1,"actual money:",p1money)
                    print("What a chance!!! You will be rewarded the money taxed:",tax)
                    p1money += tax
                    antitax1 += 1
                    tax = 0
                    print(player1,"'s money became",p1money,"$")

                elif case1 == 10:#The player lands on Box 10
                    PrintBoard()
                    if antitax1 == 1:
                        print("You won't pay tax because you already landed on the jackpot before")
                        Y = input("")
                        antitax1 = 0
                    else:
                        print("You were taxed!")
                        p1money -= int(p1money)*0.1
                        tax += int(p1money)*0.1
                        tax = int(tax)
                        p1money = int(p1money)
                        print(player1,"'s money =",p1money)
                        Y= input("")
                    PrintBox(10)
                    print(player1,"actual money:",p1money)
                    p1money *= 2
                    print(player1,"'s money is doubled:",p1money)

                elif case1 == 11:#The player lands on Box 11
                    PrintBoard()
                    if antitax1 == 1:
                        print("You won't pay tax because you already landed on the jackpot before")
                        Y = input("")
                        antitax1 = 0
                    else:
                        print("You were taxed!")
                        p1money -= int(p1money)*0.1
                        tax += int(p1money)*0.1
                        tax = int(tax)
                        p1money = int(p1money)
                        print(player1,"'s money =",p1money)
                        Y= input("")
                    PrintBox(11)
                    print(player1,"actual money:",p1money)
                    change1 = p1money
                    change2 = p2money
                    Y = input("                                         Roll the Dice!!!")
                    dice = randint(1,3)
                    if dice == 2:
                        print("Wow, You got '2'!!! Now your money will be swapped with you opponent's")
                        p1money = change2
                        p2money = change1
                        print(player1,"'s money is now",p1money,"While",player2,"'s money is now",p2money)
                    else:
                        print("Unfortunatly (or fortunatly), your money won't be swapped, you got",dice,"in the dice roll")

                elif case1 == 12:#The player lands on Box 12
                    PrintBoard()
                    PrintBox(12)
                    print(player1,"actual money:",p1money)
                    if antitax1 > 0:
                        antitax1 = 0
                    if rand == 0:
                        randomnumber = randint(0,30)
                        rand = 1
                        print("You will have to Guess the number that is hidden between 0 and 30 (inclusive) \n")
                        print("~One try, if you don't get the number right, he won't change until you do for the rest of the game")
                        guess = input("Guess the number from 0 to 30: ")
                        while guess.isdigit() == False or int(guess) not in range(31):
                            print("I asked for A Number! Within the range of course.")
                            guess = input("Guess the number within the range of [0-30]: ")
                        if randomnumber == int(guess):
                            print("You Won!!!")
                            p1money += 1000
                            print(player1,"'s money is now",p1money)
                            randomnumber = randint(0,30)
                        else:
                            print("Too bad ... It isn't the right number")
                    else:
                        print("You will have to Guess the number that is hidden between 0 and 30 (inclusive) \n")
                        print("~One try, if you don't get the number right, he won't change until you do for the rest of the game")
                        guess = input("Guess the number from 0 to 30: ")
                        while guess.isdigit() == False or int(guess) not in range(31):
                            print("I asked for A Number! Within the range of course.")
                            guess = input("Guess the number within the range of [0-30]: ")
                        if randomnumber == int(guess):
                            print("You Won!!!")
                            p1money += 1000
                            print(player1,"'s money is now",p1money)
                            randomnumber = randint(0,30)
                        else:
                            print("Too bad ... It isn't the right number")

                elif case1 == 13:#The player lands on Box 13
                    PrintBoard()
                    PrintBox(13)
                    print(player1,"actual money:",p1money)
                    print("You'll be teleported to the next 11 boxes. If you land in a box you won't get its effect")
                    case13rand = randint(1,11)
                    case1 += case13rand
                    if case1 > 15:
                        case1 -= 15
                    print(player1,"will be teleported to the Box:",case1)
                    Y = input("")
                    PrintBoard()

                elif case1 == 14:#The player lands on Box 14                                                                                                                     N
                    PrintBoard()
                    PrintBox(14)
                    print(player1,"actual money:",p1money)
                    print("GO BACK TO THE FIRST BOX!")
                    Y = input("")
                    case1 = 1
                    PrintBoard()

                elif case1 == 15:#The player lands on Box 15
                    PrintBoard()
                    PrintBox(15)
                    print(player1,"actual money:",p1money)
                    print("Do you want to spend 100 and take the risk? You will have to roll a dice and get 1 in order to win 600 Money.")
                    Y = input("type Y if you want to: ")
                    if Y == "Y" or Y == "y" and p1money >= 100:
                        p1money -= 100
                        print(player1,"'s Money is",p1money,", Good Luck!")
                        y = input("                                                  Press Enter to Roll Dices")
                        x = randint(1,3)
                        print("YOU GOT",x)
                        Y = input("")
                        if x == 1:
                            p1money += 600
                            print("CONGRATULATION! You now have",p1money,"Money!")
                        else:
                            print("Maybe next time!")
                    elif Y =="Y" or Y == "y" and p1money < 100:
                        print("You can't! You don't have enough money. Maybe next time!")
                    else:
                        print("That's pretty coward of your part")
                print("   -------------------------------------------------------",player2,"'s Turn!-------------------------------------------------------")
                Y = input("                                                 Press Enter to Roll Dices")
                dice2 = randint(1, 3)
                case2 += dice2
                if case2 > 15:
                    case2 -= 15
                print("                       Your Dice: ",dice2)

                if case2 == 1:#The player lands on Box 1
                    PrintBoard()
                    PrintBox(1)
                    print(player2,"actual money:",p2money)
                    p2money += 200
                    print("\nYou got 200$")
                    print(player2,"now have",p2money)

                elif case2 == 2:#The player lands on Box 2
                    PrintBoard()
                    PrintBox(2)
                    print(player2,"actual money:",p2money)
                    print("Players have landed on this box",T,"times before")
                    p2money += 100 * int(T)
                    T += 1
                    print(player2,"'s money became",p2money)

                elif case2 == 3:#The player lands on Box 3
                    PrintBoard()
                    PrintBox(3)
                    print(player2,"actual money:",p2money)
                    Y = input("                                             Press Enter to ReRoll Dices")
                    dice2 = randint(1, 3)
                    case2 += dice2
                    if case2 > 15:      #Corrects the position for
                        case2 -= 15     #the ReRoll (Accurately gives him the effect of each box)

###################################################           ReRoll              #############################################################
                    if case2 == 4:#The player lands on Box 4 (ReRoll)
                        PrintBoard()
                        PrintBox(4)
                        print(player2,"actual money:",p2money)
                        if landed == 0:
                            print("Choose a value for the Number 'K' ( From 0 to 20) : ")
                            K = input("What value do you assign?> ")
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            while K.isdigit() == False or int(K) not in range(21):
                                print("A Number[0-20] please")
                                K = input("A value to K ( From 0 to 20 )> ")
                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                            landed = 1
                        elif landed != 0:
                            print("What is the value of the Number? From 0 to 20")
                            Kguess = input("K = ")
                            while Kguess.isdigit() == False or int(K) not in range(21):
                                print("The value of you guess must be a Number! From 0 to 20")
                                Kguess = input("K = ")
                            if int(Kguess) == int(K):
                                print("You won!!!")
                                p2money +=400
                                print(player2,"'s money became:",p2money)
                                landed = 0
                            else:
                                print("Maybe next time")

                    elif case2 == 5:#The player lands on Box 5 (ReRoll)
                        PrintBoard()
                        PrintBox(5)
                        print(player2,"actual money:",p2money)
                        p2money = int(p2money/dice2)
                        print(player2,"'s money is now",p2money)

                    elif case2 == 6:#The player lands on Box 6 (ReRoll)
                        PrintBoard()
                        PrintBox(6)
                        print(player2,"actual money:",p2money)
                        if barrier2>0:
                            barrier2 -=1
                            print("You were saved from the loss of 200 $ by your barrier")
                            print("Barrier left:",barrier2)
                        else:
                            p2money -= 200
                            if p2money <0:
                                p2money = 0
                            print("\nYou lost 200$")
                            print(player2,"now have",p2money)
###################################################           ReRoll              #############################################################

                elif case2 == 4:#The player lands on Box 4
                    PrintBoard()
                    PrintBox(4)
                    print(player2,"actual money:",p2money)
                    if landed == 0:
                        print("Choose a value for the Number 'K' ( From 0 to 20) : ")
                        K = input("What value do you assign?> ")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        while K.isdigit() == False or int(K) not in range(21):
                            print("A Number[0-20] please")
                            K = input("A value to K ( From 0 to 20 )> ")
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        landed = 1
                    elif landed != 0:
                        print("What is the value of the Number? From 0 to 20")
                        Kguess = input("K = ")
                        while Kguess.isdigit() == False or int(K) not in range(21):
                            print("The value of you guess must be a Number! From 0 to 20")
                            Kguess = input("K = ")
                        if int(Kguess) == int(K):
                            print("You won!!!")
                            p2money +=400
                            print(player2,"'s money became:",p2money)
                            landed = 0
                        else:
                            print("Maybe next time")

                elif case2 == 5:#The player lands on Box 5
                    PrintBoard()
                    PrintBox(5)
                    print(player2,"actual money:",p2money)
                    p2money = int(p2money/dice2)
                    print(player2,"'s money is now",p2money)

                elif case2 == 6:#The player lands on Box 6                                                                                                                      A
                    PrintBoard()
                    PrintBox(6)
                    print(player2,"actual money:",p2money)
                    if barrier2>0:
                        barrier2 -=1
                        print("You were saved from the loss of 200 $ by your barrier")
                        print("Barrier left:",barrier2)
                    else:
                        p2money -= 200
                        if p2money <0:
                            p2money = 0
                        print("\nYou lost 200$")
                        print(player2,"now have",p2money)

                elif case2 == 7:#The player lands on Box 7
                    PrintBoard()
                    PrintBox(7)
                    print(player2,"actual money:",p2money)
                    barrier2 += 1
                    print("You are now protected from the",barrier2,"next lost of money")

                elif case2 == 8:#The player lands on Box 8
                    PrintBoard()
                    PrintBox(8)
                    print(player2,"actual money:",p2money)
                    print("Do you want to Gamble !?")
                    Y = input("How much?>  ")
                    while Y.isdigit() == False or p2money < int(Y):
                        print("Write a NUMBER that you can afford please!")
                        Y = input("Let me repeat, how much?>  ")
                    else:
                        p2money -= int(Y)
                        print(player2,"'s money became",p2money)
                        kakegurui = int(Y) * randint(-1,6)
                        newp2 = int(p2money) + int(kakegurui)
                        p2money = newp2
                        if p2money < 0:
                            p2money = 0
                        print(kakegurui,"will be added to your money!")
                        print(player2,"'s money became:",p2money)

                elif case2 == 9:#The player lands on Box 9                                                                                                                      M
                    PrintBoard()
                    PrintBox(9)
                    print(player2,"actual money:",p2money)
                    print("What a chance!!! You will be rewarded the money taxed:",tax)
                    p2money += tax
                    tax = 0
                    antitax2 += 1
                    print(player2,"'s money became",p2money,"$")

                elif case2 == 10:#The player lands on Box 10
                    PrintBoard()
                    if antitax2 == 1:
                        print("You won't pay tax because you already landed on the jackpot before")
                        Y = input("")
                        antitax2 = 0
                    else:
                        print("You were taxed!")
                        p2money -= int(p2money)*0.1
                        tax += int(p2money)*0.1
                        tax = int(tax)
                        p2money = int(p2money)
                        print(player2,"'s money =",p2money)
                        Y= input("")
                    PrintBox(10)
                    print(player2,"actual money:",p2money)
                    p2money *= 2
                    print(player2,"'s money is doubled:",p2money)

                elif case2 == 11:#The player lands on Box 11
                    PrintBoard()
                    if antitax2 == 1:
                        print("You won't pay tax because you already landed on the jackpot before")
                        Y = input("")
                        antitax2 = 0
                    else:
                        print("You were taxed!")
                        p2money -= int(p2money)*0.1
                        tax += int(p2money)*0.1
                        tax = int(tax)
                        p2money = int(p2money)
                        print(player2,"'s money =",p2money)
                        Y= input("")
                    PrintBox(11)
                    print(player2,"actual money:",p2money)
                    change1 = p1money
                    change2 = p2money
                    Y = input("                                         Roll the Dice!!! (Get 2 => swap money)")
                    dice = randint(1,3)
                    if dice == 2:
                        print("Wow, You got '2'!!! Now your money will be swapped with you opponent's")
                        p1money = change2
                        p2money = change1
                        print(player1,"'s money is now",p1money,"While",player2,"'s money is now",p2money)
                    else:
                        print("Unfortunatly (or fortunatly), your money won't be swapped, you got",dice,"in the dice roll")

                elif case2 == 12:#The player lands on Box 12                                                                                                                     
                    PrintBoard()
                    PrintBox(12)
                    print(player2,"actual money:",p2money)
                    if antitax2 > 0:
                        antitax2 = 0
                    if rand == 0:
                        randomnumber = randint(0,30)
                        rand = 1
                        print("You will have to Guess the number that is hidden between 0 and 30 (inclusive) \n")
                        print("~One try, if you don't get the number right, he won't change until you do for the rest of the game")
                        guess = input("Guess the number from 0 to 30: ")
                        while guess.isdigit() == False or int(guess) not in range(31):
                            print("I asked for A Number! Within the rang of course.")
                            guess = input("Guess the number within the range of [0-30]: ")
                        if randomnumber == int(guess):
                            print("You Won!!!")
                            p1money += 1000
                            print(player1,"'s money is now",p1money)
                            randomnumber = randint(0,30)
                        else:
                            print("Too bad ... It isn't the right number")
                    else:
                        print("You will have to Guess the number that is hidden between 0 and 30 (inclusive) \n")
                        print("~One try, if you don't get the number right, he won't change until you do for the rest of the game")
                        guess = input("Guess the number from 0 to 30: ")
                        while guess.isdigit() == False or int(guess) not in range(31):
                            print("I asked for A Number! Within the range of course.")
                            guess = input("Guess the number within the range of [0-30]: ")
                        if randomnumber == int(guess):
                            print("You Won!!!")
                            p1money += 1000
                            print(player1,"'s money is now",p1money)
                            randomnumber = randint(0,30)
                        else:
                            print("Too bad ... It isn't the right number")

                elif case2 == 13:#The player lands on Box 13
                    PrintBoard()
                    PrintBox(13)
                    print(player2,"actual money:",p2money)
                    print("You'll be teleported to the next 11 boxes. If you land in a box you won't get its effect")
                    case13rand = randint(1,11)
                    case2 += case13rand
                    if case2 > 15:
                        case2 -= 15
                    print(player2,"will be teleported to the Box:",case2)
                    Y = input("")
                    PrintBoard()

                elif case2 == 14:#The player lands on Box 14
                    PrintBoard()
                    PrintBox(14)
                    print(player2,"actual money:",p2money)
                    print("GO BACK TO THE FIRST BOX!")
                    Y = input("")
                    case2 = 1
                    PrintBoard()

                elif case2 == 15:#The player lands on Box 15
                    PrintBoard()
                    PrintBox(15)
                    print(player2,"actual money:",p2money)
                    print("Do you want to spend 100 and take the risk? You will have to roll a dice and get 1 in order to win 600 Money.")
                    Y = input("type Y if you want to: ")
                    if Y == "Y" or Y == "y" and p2money >= 100:
                        p2money -= 100
                        print(player2,"'s Money is",p2money,", Good Luck!")
                        y = input("                                                  Press Enter to Roll Dices")
                        x = randint(1,3)
                        print("YOU GOT",x)
                        Y = input("")
                        if x == 1:
                            p2money += 600
                            print("CONGRATULATION! You now have",p2money,"Money!")
                        else:
                            print("Maybe next time!")
                    elif Y =="Y" or Y == "y" and p2money < 100:
                        print("You can't! You don't have enough money. Maybe next time!")
                    else:
                        print("That's pretty coward of your part")
                turn -= 1
                print("   -----------------------------------------------------ROUND Number",turn,"--------------------------------------------------------------")
            if turn == 0:
                shell.write("\n                       The Game is Over, now let's see who got more money!\n","COMMENT")

                print(player1,"got",p1money,"Money..")
                print("And,",player2,"got",p2money,"Money!")
                if p1money > p2money:
                    print("                       So,",player1,"Won !!!!")
                elif p1money < p2money:
                    print("                       So,",player2,"Won !!!!")
                elif p2money == p1money:
                    print("                                Draw! What a beautiful end for two extraordinary players!")

                print("                       Do you want to replay? Write 'Y' to replay or press Enter to Stop.")

                Y = input("")
                if Y == "Y" or Y == "y":
                    print(" -----------------------------------------------------------RESTART-------------------------------------------------------------------------")

                    RESTART()
                elif Y!= "Y" or Y!= "y":
                    shell.write("\n                       Have a nice day!\n","KEYWORD")
RESTART()
