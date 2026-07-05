# Python Game Quiz with Difficulty Levels (No OOP)

def Quiz_game() :
    print(" Welcome to the Python Game Quiz!")
    print("Choose difficulty: easy - medium - hard")
    level = input(" Enter Your choice: ").lower()
    score = 0

    
    if level == "easy":                                                               #easy
        print("\nQ1: What is the output of print(2 + 3)?")
        answer = input("Your answer: ")
        if answer == "5":
            print(" Correct!")
            score += 1
        else:
            print(" Wrong! The answer is 5.")


        print("\nQ2:?")
        answer = input("Your answer: ")
        if answer.lower() == "def":
            print(" Correct!")
            score += 1
        else:
            print(" Wrong The answer is 'def'.")

   

    elif level == "medium":
        print("\nQ1: What is the output of print(len([10, 20, 30]))")
        answer = input("Your answer: ")                                                               # medium
       
        if answer == "3" :
            print(" Correct!")
            score += 1
        else:
            print(" Wrong! The answer is 3.")

        print("\nQ2: Which operator is used for floor division in Python?")
        answer = input("Your answer: ")
        if answer == "//":
            print("Correct!")
            score += 1
        else:
            print(" Wrong! The answer is //.")

   
    elif level == "hard":
        print("\nQ1: What is the output of print(bool('False'))?")
        answer = input("Your answer : ")
        if answer.lower() == "true" :
            print(" Correct!")
            score += 1
        else:
            print(" Wrong! The answer is True")                                                                 #hard

        print("\nQ2: What is the difference between @staticmethod and @classmethod ")
        answer = input("Your answer : ")

        print(" Correct if you explained that  @staticmethod does not take sel and cls, " "while @classmethod takes cls as the first argument.")

    else:
        print("Invalid choice. Please restart and choose easy, medium, or hard.")

    
    print(f"\n final score is = {score}")

Quiz_game()
