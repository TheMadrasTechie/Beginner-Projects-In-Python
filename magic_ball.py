import random
import time

answer_balls = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

def question():
    ques = input("You may ask anything you want answers for my child.")
    print("Thinking.....")
    time.sleep(random.randrange(0,5))
    print(random.choice(answer_balls))

while True:
    question()
    repeat = input("Would You like to ask any other question? (Y or N)")
    if (repeat == "n" or repeat == "N"):
        print("Let me know when you have soubts")
        break