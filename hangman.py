import random
import time
print("Welcome to Hangman Game:\n")
name  = input("Enter Your Name: ")
print("Welcome "+name+" Let's Play Hangman.")
time.sleep(1)
print("Let's Start The Game!!!!")
time.sleep(2)

def main():
    global count
    global display
    global word
    global word_val
    global already_guessed
    global length
    global game_var
    global guess_word
    guess_words = ["cat","dog","lemon","dark","netflix","messi","ronaldo"]
    guess_clue = ["a pet animal","a pet animal","a citric fruit","a web series","an OTT platform","An argentine footballer","a portugese footballer"]
    word = random.choice(guess_words)
    word_val = word
    index = guess_words.index(word)
    guess_word = guess_clue[index]
    length = len(word)
    display = '_' * length
    count = 0
    already_guessed = []
    game_var = ""
    game_func()

def play_loop():    
    global count
    count = 0
    global display
    display = ""
    global word
    word = ""
    global word_val
    word_val = ""
    global already_guessed
    already_guessed = ""
    global length
    length = 0
    global game_var
    game_var = input("Wish To Play Again? \n y = Yes , n= No")
    while game_var not in ["y", "Y","n","N"]:
        game_var = input("Wish To Play Again? \n y = Yes , n= No")
    if (game_var == "y")or(game_var == "Y"):
        main()
    elif (game_var == "n")or(game_var == "N"):
        print("Thanks For Playing! \n Do Come Again!!!!")
        exit()

def game_func():
    global count
    global display
    global word
    global word_val
    global already_guessed    
    global game_var
    global guess_word
    limit = 5
    print("This is the description: ",guess_word)
    guess = input("This is the Word: "+display.replace("_"," _ ")+"\nEnter Your Guess:")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2:
        print("Invalid Input, Try Again \n")
        game_func()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index]+"_"+word[index+1:]
        display =  display[:index]+guess+display[index+1:]
        print(display+"\n")
    elif guess in already_guessed:
        print("Try Another Letter. \n")
    else:
        count += 1
        if count ==1:
            time.sleep(1)
            print(" ______\n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print(" |     \n")
            print("_|_    \n")
            print("limit "+str(count)+"reached")
        elif count ==2:
            time.sleep(1)
            print(" ______ \n")
            print(" |     |\n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print("_|_     \n")
            print("limit "+str(count)+"reached")
        elif count ==3:
            print(" ______ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print(" |      \n")
            print("_|_     \n")
            time.sleep(1)
            print("limit "+str(count)+"reached")
        elif count ==4:
            print(" ______ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     O \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |      \n")
            print(" |      \n")
            print("_|_     \n")
            time.sleep(1)
            print("limit "+str(count)+"reached")
        if count ==5:
            print(" ______ \n")
            print(" |     |\n")
            print(" |     |\n")
            print(" |     O \n")
            print(" |    /|\ \n")
            print(" |     |\n")
            print(" |    / \ \n")
            print(" |      \n")
            print("_|_     \n")
            time.sleep(1)
            print("limit "+str(count)+"reached")
            print("The Hangman is dead")
            print("The Correct Word is :",word_val)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word!!")
        play_loop()
    elif count != limit:
        game_func()
main()