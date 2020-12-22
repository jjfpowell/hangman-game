import random
import time
import words
import re
import sys

def welcome():
    print("Welcome to Hangman. Please bear with us while we select a word!")
    global selected
    time.sleep(2)
    selected=random.choice(words.words)
    while "-" in selected or " " in selected:
        selected=random.choice(words.words)
    print("Complete! \nPlease see your clue below:")
    global clue
    clue=len(selected)*"_ "
    print(clue)
    play_round()

def play_round():
    global lives
    lives=0
    attempts=0
    guesses=[]
    global selected_list
    selected_list=[]
    for char in selected:
        selected_list.append(char)
    global clue2
    clue2=clue
    print("Use 'quit' to quit, 'restart' to restart or 'guesses' to see\
 your guesses so far.")
    while lives<9 and "_" in clue2:
        k=0 
        while k!=1:
            guess=input("Please enter your guess: ").lower()
            if guess=="restart":
                welcome()
            elif guess=="quit":
                sys.exit(0)
            elif guess=="guesses":
                print("So far you have guessed:",guesses)
            elif not re.match("^[a-z]*$",guess):
                print("Error! Only letters a-z allowed!")
            elif len(guess)>1:
                print("Error! Only 1 character at a time please!")
            else:
                k+=1
        if guess in guesses:
            print("This letter has already been guessed")
            attempts+=1
        elif guess in selected:
                print("Correct!")
                update_clue(guess,clue2)
                guesses.append(guess)
                print(clue2)
                attempts+=1
        elif guess not in selected:
            incorrect_guess(lives)
            lives+=1
            attempts+=1
            guesses.append(guess)
    if lives==9:
        print("Oh no! Your hangman has been hung. The word you were looking for was '%s'."%(selected))
    else:
        print("Congratuations! You guessed '%s' in just %d attempts!"%(selected,attempts))
    i=0
    while i==0:
        again=input("Would you like to play again? (yes or no) ").lower()
        if again=="yes" or again=="no":
            i+=1
    if again=="yes":
        welcome()
    else:
        sys.exit(0)
            
def update_clue(user_input,hint):
    count=0
    index_list=[]
    for x in selected_list:###Gets the index all matching characters
        if x==user_input:
            index_list.append(count)
        count+=1
    clue_list=[]
    for char in hint:
        if char != " ":
            i=char.strip()
            clue_list.append(i)
    for x in index_list:
        clue_list[x]=str(user_input)
    global clue2
    clue2=" ".join(clue_list)
    
def incorrect_guess(num):
    if num==0:
        print("Incorrect!")
        print("__")
    elif num==1:
        print("Incorrect!")
        print("__ __")
    elif num==2:
        print("Incorrect!")
        print("  |\n__|__")
    elif num==3:
        print("Incorrect!")
        print("  |\n  |\n  |\n__|__")
    elif num==4:
        print("Incorrect!")
        print("  __\n  |\n  |\n  |\n__|__")
    elif num==5:
        print("Incorrect!")
        print("  ____\n  |\n  |\n  |\n__|__")
    elif num==6:
        print("Incorrect!")
        print("  ____\n  |   O\n  |\n  |\n__|__")
    elif num==7:
        print("Incorrect!")
        print("  ____\n  |   O\n  |   +\n  |\n__|__")
    elif num==8:
        print("Incorrect!")
        print("  ____\n  |   O\n  |   +\n  |   ^\n__|__")

welcome()
