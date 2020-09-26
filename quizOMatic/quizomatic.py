#!/usr/local/python

# name: quizomatic.py
# purpose: quiz game
# author: Henry E
# date: 7/11/2020

#imports

import requests

# Getting Questions category difficulty

def getQuizParams ():
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
            print("9 = General Knowledge \n \
10 = Entertainment: Books \n \
11 = Entertainment: Film \n \
12 = Entertainment: Music \n \
13 = Entertainment: Musicals & Theatres \n \
14 = Entertainment: Television \n \
15 = Entertainment: Video Games \n \
16 = Entertainment: Board Games \n \
17 = Science & Nature \n \
18 = Science: Computers \n \
19 = Science: Mathematics \n \
20 = Mythology \n \
21 = Sports \n \
22 = Geography \n \
23 = History \n \
24 = Politics \n \
25 = Art \n \
26 = Celebrities \n \
27 = Animals \n \
28 = Vehicles \n \
29 = Entertainment: Comics \n \
30 = Science: Gadgets \n \
31 = Entertainment: Japanese Anime & Manga  \n \
32 = Entertainment: Cartoon & Animations")
            category = input("Choose The Category by number. 9 - 32: ")
            if category.isdigit():
                if int(category) >= 9 and int(category) <= 32:
                    categoryNotValidated = False
                    print("Category: ",category)
                else:
                    print("Select a number from 9 - 32")
            else:
                print("Select a number from 9 - 32")
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
            print(difficulty, category, num_Qs)
            valid = input("Is this correct? Y/N: ")
            if valid in ["Y","N","y","n","Yes","No","yes","no"]:
                if valid in ["Y", "y", "Yes", "yes"]:
                    validNotValidated = False
                    paramsNotValidated = False
                else:
                    print("Let's try again. ;D")
                    validNotValidated = False
            else:
                print("Type Yes or No")

    return(difficulty, category, num_Qs)



#requesting questions from OpenTDB

def getQuizQuestions (difficulty, category, num_Qs):
    payload = {"amount" : num_Qs , "category" : category , "difficulty" : difficulty }
    r = requests.get("https://opentdb.com/api.php" , params = payload)
    print(r.url)
    print(r.text)
    return(r)


#main

difficulty , category , num_Qs = getQuizParams()
getQuizQuestions(difficulty, category, num_Qs)

