#!/usr/local/python

# name: quizomatic.py
# purpose: quiz game
# author: Henry E
# date: 7/11/2020

# imports
import random
import requests


# Getting Questions category difficulty

def getQuizParams(debug):
    if debug:
        print("Executing getQuizParams")
    paramsNotValidated = True
    while paramsNotValidated:

        difficultyNotValidated = True
        while difficultyNotValidated:
            difficulty = input("How Difficult? Easy, Medium, or Hard: ")
            difficulty = difficulty.lower()
            if difficulty in ["easy", "medium", "hard"]:
                difficultyNotValidated = False
                print("Difficulty: ", difficulty)
            else:
                print("Enter Easy, Medium, or Hard")

        categoryNotValidated = True
        while categoryNotValidated:
            print("Quiz Categories:")
            print("1 = General Knowledge \n \
2 = Entertainment: Books \n \
3 = Entertainment: Film \n \
4 = Entertainment: Music \n \
5 = Entertainment: Musicals & Theatres \n \
6 = Entertainment: Television \n \
7 = Entertainment: Video Games \n \
8 = Entertainment: Board Games \n \
9 = Science & Nature \n \
10 = Science: Computers \n \
11 = Science: Mathematics \n \
12 = Mythology \n \
13 = Sports \n \
14 = Geography \n \
15 = History \n \
16 = Politics \n \
17 = Art \n \
18 = Celebrities \n \
19 = Animals \n \
20 = Vehicles \n \
21 = Entertainment: Comics \n \
22 = Science: Gadgets \n \
23 = Entertainment: Japanese Anime & Manga  \n \
24 = Entertainment: Cartoon & Animations")
            category = input("Choose The Category by number. 1 - 24: ")
            if category.isdigit():
                category = int(category) + 8
                if int(category) >= 9 and int(category) <= 32:
                    categoryNotValidated = False
                    print("Category: ", int(category) - 8)
                else:
                    print("Select a number from 1 - 24")
            else:
                print("Select a number from 1 - 24")
        num_QsNotValidated = True
        while num_QsNotValidated:
            num_Qs = input("How Many Questions? 10-50: ")
            if num_Qs.isdigit():
                if int(num_Qs) >= 10 and int(num_Qs) <= 50:
                    num_QsNotValidated = False
                else:
                    print("Type a number between 10 and 50")
            else:
                print("Type a whole number")
        validNotValidated = True
        while validNotValidated:
            print(difficulty, int(category) - 8, num_Qs)
            valid = input("Is this correct? Y/N: ")
            if valid in ["Y", "N", "y", "n", "Yes", "No", "yes", "no"]:
                if valid in ["Y", "y", "Yes", "yes"]:
                    validNotValidated = False
                    paramsNotValidated = False
                else:
                    print("Let's try again. ;D")
                    validNotValidated = False
            else:
                print("Type Yes or No")

    return (difficulty, category, num_Qs)


# requesting questions from OpenTDB

def getQuizQuestions(difficulty, category, num_Qs, debug):
    payload = {"amount": num_Qs, "category": category, "difficulty": difficulty}
    r = requests.get("https://opentdb.com/api.php", params=payload)
    if debug:
        print(r.url)
    if debug:
        print(r.text)
    return (r.json())

def proccesQList(quizQuestions, debug):
    for metaQuestion in quizQuestions['results']:
        if debug:
            print("Category: ", metaQuestion['category'])
            print("Type: ", metaQuestion['type'])
            print("Question: ", metaQuestion['question'])
            print("Correct answer: ", metaQuestion['correct_answer'])
            print("Incorrect answer: ", metaQuestion['incorrect_answers'])
        if metaQuestion['type'] == "multiple":
            qAnswer = promptMultiQ(metaQuestion, debug)
        else:
            qAnswer = promptBooleanQ(metaQuestion, debug)
        #print(qAnswer)
    return

def promptMultiQ(metaQuestion, debug ):
    print("Question: ", metaQuestion['question'])
    if debug:
        print("Correct answer: ", metaQuestion['correct_answer'])
        print("Incorrect answer: ", metaQuestion['incorrect_answers'])
    #allAnswers = metaQuestion['incorrect_answers'].append(metaQuestion['correct_answer'])
    allAnswers = metaQuestion['incorrect_answers']
    if debug:
        print("Type allAnswers-1", type(allAnswers))
    allAnswers.append(str(metaQuestion['correct_answer']))
    if debug:
        print("Type allAnswers-2", type(allAnswers))
        print(allAnswers)
    random.shuffle(allAnswers)
    answerPosition = 0
    for answer in allAnswers:
        if answer == metaQuestion['correct_answer']:
            correctAnswer = answerPosition
        else:
            answerPosition = answerPosition + 1
    print(allAnswers)
    # Then I need to add a function where it asks the user for an answer. 1-4. It then compares that answer to the real answer. 
    userAnswer = input("Choose an answer with a number 1-4: ")
    printedAnswer = correctAnswer + 1
    if userAnswer.isdigit():
        userAnswer = int(userAnswer) - 1
    if userAnswer == correctAnswer:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The correct answer was" , printedAnswer)
    return(correctAnswer)

def promptBooleanQ(metaQuestion, debug):
    print("Question: ", metaQuestion['question'])
    correctAnswer = metaQuestion['correct_answer']
    print("True or False")
    #Then I need to add a function where it asks the for an answer. True or false. It then compares that answer to the real answer.
    userAnswer = input("Choose True or False: ")
    
    if userAnswer == correctAnswer:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The correct answer was" , correctAnswer)
    return(correctAnswer)

# main

debug = False
difficulty, category, num_Qs = getQuizParams(debug)
quizQuestions = getQuizQuestions(difficulty, category, num_Qs, debug)
proccesQList(quizQuestions, debug)
