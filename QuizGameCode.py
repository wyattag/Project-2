import random
import time
import threading
import os
import keyboard
# Variables
name = input("What is your name? ")
Points = 0
CorrectAwnserPoints = 1
keepPlaying = 0
running = True
WhilePlaying = True

# Greeting function
def greet(name):
    print(f"Hello, {name}!")

# Arrays
QuestionArray = [
    "What is the tallest animal in the world?",
    "Which bird doesn't fly?",
    "Which animal lives underwater?",
    "What is the largest planet in our solar system?",
    "Which gas do plants absorb from the air?",
    "What is the capital of France?",
    "Who wrote Romeo and Juliet?",
    "How many legs does a spider have?",
    "How many continents are there on Earth?",
    "Which ocean in the largest?",
    "What planet is closest to the sun?",
    "How many sides does a hexagon have?"
]

ChoicesArray = [
    "1: Bear, 2: Ant, 3: Giraffe",
    "1: Toyota Camry, 2: Penguin, 3: Seagull",
    "1: Jellyfish, 2: Deer, 3: Triceratops",
    "1: Earth, 2: Jupiter, 3: Mars",
    "1: Oxygen, 2: Nitrogen, 3: Carbon Dioxide",
    "1: Madrid, 2: Paris, 3: Rome",
    "1: William Shakespeare, 2: Charles Dickens, 3: Mark Twain",
    "1: 6, 2: 8, 3: 10",
    "1: 5, 2: 8, 3: 7",
    "1: Atlantic, 2: Pacific, 3: Indian",
    "1: Mercury, 2: Venus, 3: Mars",
    "1: 5, 2: 6, 3:8"
]

AnswerArray = ["3", "2", "1", "2", "3", "2", "1", "2", "3","2", "1","2"]

usedQuestions = []

positiveResponseArray = ["That's amazing!", "That's great!", "Good job!", "Wow!"]
negativeResponseArray = ["Too bad", "Better shot next time", "You tried", "Almost!"]

# Timeout function
def timeout():
    print("Time ran out,", random.choice(negativeResponseArray), "Score:", Points)
    os._exit(0)

# Get unused question
def getQuestion():
    while True:
        questionNum = random.randint(0, len(QuestionArray) - 1)
        if questionNum not in usedQuestions:
            usedQuestions.append(questionNum)
            return questionNum

# Start
greet(name)
print("Welcome to our game!")
print("Answer the questions to earn points. You have 20 seconds per question. Faster answers earn more points!")
print("Press any key to start playing!")



while running:
    fiveQuestionLoop = 1
    usedQuestions = []  # Reset for each round
    WhilePlaying = True

    while WhilePlaying:
        while fiveQuestionLoop <= 5:
            questionNum = getQuestion()

            print(f"\n#{fiveQuestionLoop}) {QuestionArray[questionNum]}")
            print(ChoicesArray[questionNum])

            Timer = threading.Timer(20, timeout)
            Timer.start()

            startTime = time.time()
            userInput = keyboard.wait("a")
            
            Timer.cancel()
            timeTaken = time.time() - startTime

            if userInput == AnswerArray[questionNum]:
                if timeTaken < 5:
                    Points += 3
                elif timeTaken < 10:
                    Points += 2
                else:
                    Points += 1
                print("Correct Answer,", random.choice(positiveResponseArray))
            else:
                print("Wrong Answer,", random.choice(negativeResponseArray))

            fiveQuestionLoop += 1

        keepPlaying = input("\nDo you want to continue? Y or N: ").upper()
        if keepPlaying == "Y":
            print("Next round starting...")
            WhilePlaying = True
            break
        else:
            print(random.choice(positiveResponseArray), "Your final score:", Points)
            WhilePlaying = False
            running = False
            print("Thanks for playing!")
            break
