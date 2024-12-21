
# Online Python - IDE, Editor, Compiler, Interpreter

import random 
import string
 
def hintAssort(name):
    if name.upper() == "ORANGE":
        print("Hint: It's a color")
    if name.upper() == "MEXICO":
        print("Hint: Origin of great food")
    if name.upper() == "HARRY":
        print("Hint: Brilliant!")
    if name.upper() == "JUSTIN":
        print("Hint: someone cool :)")
    if name.upper() == "LIZETTE":
        print("Hint: love of my life")
    if name.upper() == "HAMILTON":
        print("Hint: Not gonna waste my shot!")
    if name.upper() == "HOGWARTS":
        print ("Hint: DUN DUN DU DU DUN DU DUUUUN DUUUUUNNNNNN")
list = ["ORANGE", "MEXICO", "HARRY", "HOGWARTS", "JUSTIN", "LIZETTE", "HAMILTON"]

#head = [
#[" ----"],
#["/    "],
#["|     |"],
#["\    /"],
#["----"],
#]
#for x in range(len(head)):
#    print(str(head[x])[2:-2])
bodya = ["HEAD", "LEFT_ARM", "RIGHT_ARM", "LEFT_LEG", "RIGHT_LEG"]


running  = True


# DRAW HANGMAN
# DO IF STATEMENTS THAT FOLLOW IF YOU GET IT WRONG, HANGMAN BODY PART BECOMES BLUE 
# PUT DOWN POSSIBLE GUESSES, HINTS, TEXTS
while running:
    
 
    print("Welcome to Hangman! :")
    print("+-----------------+")
    end = 'Y'
    while(end.upper() != 'N'):
        body = bodya.copy()
        newWord = random.choice(list)
        hintAssort(newWord)
        needRight = len(newWord)
        haveRight = 0
        currentWord = []
        print("Body Parts: ", body)
        print("Your word has", len(newWord), "letters!")
        for i in range (len(newWord)):
            print("__", " ", end = "")
        
        print("\n")
        letter = input("Make A Guess:")
        game = True
        letters = []
        while(game):
            j = 0
            right = False
            while j < len(newWord) or right == False:
                if(j == len(newWord)):
                    break
                if(letter.upper() == newWord):
                    haveRight = len(newWord)
                    break
                if letter.upper() == newWord[j]:
                    haveRight = haveRight + 1
                    print("You are right!")
                    letters.append(letter)
                    currentWord.append(newWord[j])
                    right = True
                    break
                elif letter.upper() != newWord[j]:
                    j = j+1 
            if(right == False and haveRight != len(newWord)):
                print("Wrong! You lost a limb")
                body.remove(random.choice(body))
                print("Body Parts: ", body)
            
            if(haveRight == len(newWord)):
                print("You won! Good job!")
                end = input("Wanna play again? (Y/N)")
                Game = False
                break
            if(body == []):
                print("You lost!")
                end = input("Wanna play again? (Y/N)")
                Game = False
                break
            print ("Your letters: ", letters)
            if len(currentWord) >= 0:
                for i in range (len(currentWord)):
                    print(currentWord[i], "  ", end='')
            print('\n', sep='')
            for i in range (len(newWord)):
                print("__", " ", end = "")
            print('\n', sep='')
            letter = input("Make another guess: ")
     

                
