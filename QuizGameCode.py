import random
import time
import threading
import os

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
    "A: Bear, B: Ant, C: Giraffe",
    "A: Toyota Camry, B: Penguin, C: Seagull",
    "A: Jellyfish, B: Deer, C: Triceratops",
    "A: Earth, B: Jupiter, C: Mars",
    "A: Oxygen, B: Nitrogen, C: Carbon Dioxide",
    "A: Madrid, B: Paris, C: Rome",
    "A: William Shakespeare, B: Charles Dickens, C: Mark Twain",
    "A: 6, B: 8, C: 10",
    "A: 5, B: 8, C: 7",
    "A: Atlantic, B: Pacific, C: Indian",
    "A: Mercury, B: Venus, C: Mars",
    "A: 5, B: 6, C:8"
]

AnswerArray = ["C", "B", "A", "B", "C", "B", "A", "B", "C","B", "A","B"]

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
            userInput = input("Your answer: ").upper()
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
