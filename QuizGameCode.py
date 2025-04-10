# initialization
import random
import time
import threading
import os

# To Do List:
# 1) Implement giving score based on time remaining
# 2) Add more questions & answers  
# 3) not ask the same question twice (pull questions from bag)
# 4) add function (maybe choosing the question our of a bag)

Points = 5
CorrectAwnserPoints = 1
keepplaying = 0
running = True

QuestionArray = [
    "What is the tallest animal in the world?",
    "Which bird doesn't fly?",
    "Which animal lives underwater?",
    "What is the largest planet in our solar system?",
    "Which gas do plants absorb from the air?"
]

ChoicesArray = [
    "A: Bear, B: Ant, C: Giraffe",
    "A: Toyota Camry, B: Penguin, C: Seagull",
    "A: Jellyfish, B: Deer, C: Triceratops",
    "A: Earth, B: Jupiter, C: Mars",
    "A: Oxygen, B: Nitrogen, C: Carbon Dioxide"
]

AnswerArray = ["C", "B", "A", "B", "C"]
WhilePlaying = True

positiveresponseArray = ["that's amazing!", "that's great!", "good job!","wow!"]
negitiveresponseArray = ["too bad"," better shot next time", "you tried","you're a failure"]
def timeout():
    print("time ran out,",negitiveresponseArray[random.randint(0,3)]," score:", Points)                     #change when adding more negitive responses 
    os._exit(0)
    

#Start
print("Welcome to our game")
print("Answer the questions to earn points. There are 5 points and 5 questions you will have a time limit to answer each question. If you enter an incorrect answer time will be deducted. The amount of time you will have resets at the start of the new question")
while running == True:
    fiveQuestionLoop = 1
    while WhilePlaying == True:
        Timer = threading.Timer(20, timeout)
        Timer.start()
        while fiveQuestionLoop <= 5:
            QuestionNum = random.randint(0,4)                                             #change when adding more questions
            print("#",fiveQuestionLoop,")",QuestionArray[QuestionNum], fiveQuestionLoop)
            print(ChoicesArray[QuestionNum])
            userInput = input("Your answer: ").upper()
            if userInput == AnswerArray[QuestionNum]:
                Points += 1
                print("Correct Awnser")
            elif userInput != AnswerArray[QuestionNum]:
                print("try again")
            fiveQuestionLoop += 1
        Timer.cancel()
        break
    
    
    #timeLeft = threading.Timer
    #if timeLeft == time.time:
    #    CorrectAwnserPoints += 3
    #elif timeLeft == 6:
    #    CorrectAwnserPoints += 2
    #Points += CorrectAwnserPoints
    #CorrectAwnserPoints = 1
    Timer.cancel()
    keepplaying = input("do you want to continue? Y or N") 
    if keepplaying == "Y":
        print("Next question:")
        WhilePlaying == True
    elif keepplaying == "y":
        print("Next question:")
        WhilePlaying == True
    else:
        print(positiveresponseArray[random.randint(0,3)], "You're score:",Points)                     #change when adding new positive responses 
        WhilePlaying == False
        running == False
        print("Thanks for playing!")
        break
