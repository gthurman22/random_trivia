#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Define the quiz questions and answers
questions = [
    ("What are the most common ingredients for a green tea shot?", "whisky, peach schnapps, sprite"),
    ("Which country consumes the most chocolate per capita?", "Switzerland"),
    ("What was the first toy to be advertised on TV?", "Mr. Potato Head"),
    ("What is the name of the Earth's largest ocean?", "pacific"),
    ("Which country produces the most coffee in the world?", "Brazil"),
    ("Which skateboarder invented the kickflip?", "rodney mullen"),
    ("Time for a pun... Why don't keyboards sleep? Because they have two...", "shifts"),
    ("What country has the most vending machines?", "Japan"),
    ("What object was taken outside to be smashed with a baseball bat in the movie Office Space?", "copier"),
    ("What state did Ellie and Joel travel to in The Last of Us to find his brother Tommy?", "Wyoming"),
    ("Another pun...What did the green grape say to the purple grape?", "breathe, you idiot!"),
    ("A boiled egg in the morning is really hard to...", "beat"),
    ("It doesn't matter how much you push the envelope, it'll still be...", "stationary"),
    ("The Magician got frustrated and pulled his____out", "hare"),
    ("Newspaper headline reads: Cartoonist found dead at home, details are...", "sketchy"),
]
  #Above, what we did is added a loop around each question  eg; [questions here, close with bracket]
    #We did this so a user can keep trying until they get the right answer, or choose to skip

def play_game():
    #instructions for starting the game
    print("Welcome to the random quiz!")
    
    while True:
        playing = input("Do you want to play? Yes/No")
        if playing.lower() == "yes":
            break
        elif playing.lower() == "no":
            print("Party pooper")
            return
    
    print("Okay! Let's play :)")
    score = 0
    
    for question, answer in questions:
        while True:
            user_answer = input(question + " (Type 'skip' to skip the question.)\n")
            if user_answer.lower() == "skip":
                break
            elif user_answer.lower() == answer.lower():
                print("Correct!")
                score += 1
                break
            else:
                print("Incorrect. Please try again or type 'skip' to move on.")
    
    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / len(questions)) * 100) + "%.")

    restart()

def restart():
    response = input("Do you want to restart? (y/n) ")
    if response.lower() == "y":
        play_game()
    else:
        print("Party Pooper!")

play_game()


# In[ ]:





# In[ ]:




