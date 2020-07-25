#!/usr/local/python

# name: quizomatic.py
# purpose: quiz game
# author: Henry E
# date: 7/11/2020

# Getting Questions category difficulty

def getQuizParams ():
    paramsNotValidated = True
    while paramsNotValidated:

        difficultyNotValidated = True
        while difficultyNotValidated:
            difficulty = input("How Difficult? On a scale 1-10. Whole Numbers Only ")
            if difficulty.isdigit():
                if int(difficulty) >= 1 and int(difficulty) <= 10:
                    difficultyNotValidated = False
                    print("Difficulty: ", difficulty)
                else:
                    print("Type a number between 1-10")
            else:
                print("Type a whole number")

        categoryNotValidated = True
        while categoryNotValidated:
            category = input("What Category? Food, Sports, Movies.")
            if category in ["Food", "Sports", "Movie"]:
                categoryNotValidated = False
                print("Category: ",category)
            else:
                print("Select a option from Food, Sports, Movies")

        num_QsNotValidated = True
        while num_QsNotValidated:
            num_Qs = input("How Many Questions? 10-50")
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
            valid = input("Is this correct? Y/N")
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


#