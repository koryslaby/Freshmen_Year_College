# this code is going to ask simple math questions and tell if
# the usser input is correct
import random
correct = 0
failed = 0


def start_directions():
    print("Answer the given math problems:\n")


def math_question():
    global correct
    global failed
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    question = input("what is {0} * {1}?".format(x, y))
    if question == str(x * y):
        print("you are correct")
        correct += 1
        print("\n your score is:")
        print("failed: {0}, correct: {1}\n".format(failed, correct))
        math_question()
    else:
        print("you are wrong")
        print("the actual answer is {0}".format(x * y))
        failed += 1
        print("\n your score is:")
        print("failed: {0}, correct: {1}\n".format(failed, correct))
        math_question()


def medium_math_question():
    global correct
    global failed
    x = random.randint(3, 15)
    y = random.randint(3, 15)
    question = input("what is {0} * {1}?".format(x, y))
    if question == str(x * y):
        print("you are correct")
        correct += 1
        print("\n your score is:")
        print("failed: {0}, correct: {1}\n".format(failed, correct))
        medium_math_question()
    else:
        print("you are wrong")
        print("the actual answer is {0}".format(x * y))
        failed += 1
        print("\n your score is:")
        print("failed: {0}, correct: {1}".format(failed, correct))
        medium_math_question()

def hard_math_question():
    global correct
    global failed
    x = random.randint(3, 30)
    y = random.randint(3, 30)
    question = input("what is {0} * {1}?".format(x, y))
    if question == str(x * y):
        print("you are correct")
        correct += 1
        print("\n your score is:")
        print("failed: {0}, correct: {1}\n".format(failed, correct))
        hard_math_question()
    else:
        print("you are wrong")
        print("the actual answer is {0}".format(x * y))
        failed += 1
        print("\n your score is:")
        print("failed: {0}, correct: {1}".format(failed, correct))
        hard_math_question()


def pick_level():
    print("How would you like to play?")
    x = input("Easy, Medium, Hard:")
    if x == "Easy":
        math_question()
    if x == "Medium":
        medium_math_question()
    if x == "Hard":
        hard_math_question()


start_directions()
pick_level()
