import random
import time
import json
import os

Number_Guessing_Game = os.path.join(os.path.dirname(__file__), "Number_Guessing_Game.json")

if not os.path.exists(Number_Guessing_Game):
    with open(Number_Guessing_Game,"w") as f:
        json.dump([],f)

def add_history(attempts,duration):
    with open(Number_Guessing_Game,"r") as f:
        score=json.load(f)
    new_score={
        "id" : len(score)+1,
        "attempts" : attempts,
        "duration" : round(duration,2)
               }

    score.append(new_score)

    with open(Number_Guessing_Game,"w") as f:
        json.dump(score,f,indent=4)

def show_high_score():
    with open(Number_Guessing_Game,"r") as f:
        score=json.load(f)
    best_score=min(score, key=lambda x: (x["attempts"], x["duration"]))
    print(f"Best Record: {best_score["attempts"]} guesses | Duration: {best_score["duration"]}")

def hint(number):
    if number % 2 == 0:
        num_status="even"
        num_status1="divided by 2"
    elif number % 2 != 0:
        num_status="odd"
    if number % 3 == 0:
        num_status1="divided by 3"
    elif number % 5 == 0 :
        num_status1="divided by 5"
    elif number % 7 == 0 :
        num_status1="divided by 7"
    else:
        num_status1=num_status
    show_hint=random.randint(1,2)
    if show_hint==1:
        print(f"The number is an {num_status} number")
    elif show_hint==2:
        print(f"The number is {num_status1}")
    
def output():
    chances=0
    status=False
    number=random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print()
    print("*"*40)
    print()
    print("""Please select the difficulty level : 
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")
    print("*"*40)
    print()
    level=int(input("Select Level : "))
    if level == 1  :
        print("-"*40)
        print("Great! You have selected the Easy difficulty level.")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 10 chances to guess the correct number.")
        chances=10
        game(number,chances,status)
    elif level == 2 :
        print("-"*40)
        print("Great! You have selected the Medium difficulty level.")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 5 chances to guess the correct number.")
        chances=5
        game(number,chances,status)
    elif level == 3 : 
        print("-"*40)
        print("Great! You have selected the Hard difficulty level.")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 3 chances to guess the correct number.")
        chances=3
        game(number,chances,status)
    else :
        print("Invalid! Select the level!")
        print()
        output()

def game(number,chances,status):
    print()
    print("----- Game Start ! -----")
    start_time = time.perf_counter()
    for i in range (chances):
        while True:
            guess=input("Enter your guess : ")
            try:
                guess=int(guess)
                break
            except:
                print("Invalid input! Your guess should be a number.")
        if guess > number :
            print(f"Incorrect! The number is less than {guess}.")
            status=False
            print()
        elif guess < number :
            print(f"Incorrect! The number is greater than {guess}.")
            status=False
            print()
        elif guess == number :
            end_time = time.perf_counter()
            duration=end_time-start_time
            add_history(i+1,duration)
            print(f"Congratulations! You guessed the correct number in {i+1} attempts within {duration:.2f} seconds!")
            show_high_score()
            status=True
            break
        if chances//2 == i and status == False:
            while True:
                want=input("Want a clue? (Yes/No) : ")
                if want == "Yes" :
                    hint(number)
                    break
                elif want == "No" :
                    break
                else :
                    print(f"Invalid Input!")
         
    if status == False :
        print(f"Game Over! You failed after {chances} attempts!")
        print(f"The correct number is {number}")
   
    print()
    while True:
        play=input("Play again (Yes/No) : ")
        if play == "Yes" :
            print()
            output()
            break
        elif play == "No" :
            print()
            print("~~~ Thank you for playing! ~~~")
            exit()
        else:
            print("Invalid Input! Try Again!")

output()