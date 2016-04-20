import questions_and_statements as qs
import lists as li
score = 0


def question1():
    global score
    question = input("On a scale of 1 to 10 how would you rate yourself\
 Envionmentaly?\n    1 being the best    10 being the wrost>>>")
    if int(question) > 5 and int(question) <= 10:
        score += int(str(question))
        print(qs.statement2)
        li.improves()
        print("\nyour score is {0}".format(score))
    if int(question) > 10:
        score += 10
        print(qs.statement3)
        li.improves()
        print("\nyour score is {0}".format(score))
    if int(question) <= 5:
        print(qs.statement4)
        print("\nYou probally do some of these things.")
        li.improves()
        score += int(str(question))
        print("\nyour score is {0}".format(score))


def question2():
    global score
    question = input("\nYes or No please. Have you littered in the last Month?")
    x = str(question)
    if x == "no" or x == "No":
        print(qs.statement5)
        print("\nyour score is {0}".format(score))
    elif x == "yes" or x == "Yes":
        print(qs.statement6)
        score += 2
        print("\nyour score is {0}".format(score))
    else:
        print('Check spelling and try again!')
        question2()


def question3():
    global score
    question = input("\nYes or No please. Have you littered in the last week?")
    x = str(question)
    if x == "no" or x == "No":
        print(qs.statement7)
        print("\nyour score is {0}".format(score))
    elif x == "yes" or x == "Yes":
        print(qs.statement8)
        score += 10
        print("\nyour score is {0}".format(score))
    else:
        print('Check spelling and try again!')
        question3()

# question 4 in q and s
def fact1():
    print("Facts For Thoughts!")
    question = input("\nHow many people are in the world today(ex.10000000)")
    if int(question) > 1000000:
        print(qs.statement9)
        people = int(question) * 2
        print("\nIf everyone in the world littered 2 things:")
        print("\nThat would meen there are {0} items of trash floating".format(people))
        print("around out there. It doesnt just disapear when you stop")
        print("seeing it.")
        li.trash()
    else:
        print("theres more people than that!")
        print('try again')
        fact1()


def question5():
    global score
    question = input("\nIf having the choice would you.. - A ride\
 your bike or - B Take the Car?")
    if str(question) == 'A' or str(question) == 'a':
        print(qs.statement10)
        print(li.travelways())
        print('Your score is {0}'.format(score))
    elif str(question) == 'B' or str(question) == 'b':
        print(qs.statement11)
        print(li.travelways())
        score += 3
        print('Your score is {0}'.format(score))
    else:
        print('Check spelling and try agian')
        question5()


glo = ()


def question6():
    global score
    global glo
    question = input("\nDo you Ride\Drive ATV's?(Yes or No)\n---------\
-------------------------\n\n")
    x = str(question)
    glo = question
    if x == "yes" or x == "Yes":
        print(qs.statement12)
        question2 = input("\nHow much do you ride\drive ATV's\
 (Alot, Kinda Alot, Not Much)")
        print('-----------------------------------------------')
        q = str(question2)
        if q.upper() == 'ALOT' or q.upper() == 'A LOT':
            score += 6
            print('\nYour score is {0}'.format(score))
        elif q.upper() == "KINDA ALOT" or q.upper() == "KINDA A LOT":
            score += 4
            print('\nYour score is {0}'.format(score))
        elif q.upper() == "NOT MUCH":
            score += 3
            print('\nYour score is {0}'.format(score))
        question7()
    elif x == 'no' or x == 'No':
        print(qs.statement13)
        print('\nYour score is {0}'.format(score))

    else:
        print("Check spelling and try agian!")
        question6()


def question7():
    global score
    global glow
    print(qs.statement14)
    glow = str(glo)
    if glow == "Yes" or glow == "yes":
        print('------------------------------')
        question = input("\nAre you carefull about where you ride?(yes or no)")
        y = str(question)
        if y.lower() == "yes":
            score += 2
            print("\nGood it is very important to not distroy Habitat's")
            print(qs.statement15)
            print("Your score is {0}".format(score))
        elif y.lower() == "no":
            print(qs.statement15)
            score += 10
            print("Your score is {0}".format(score))
    elif glow == "no" or glow == "No":
        print(qs.statement15)


def end():
    global score
    print('\nThe program is over lets see were you place at.\n\n')
    print(' ' * 10, 'Highest score is 41\n\n')
    print(' ' * 10, 'Your score is {0}\n\n'.format(score))
    print(' ' * 10, 'the lowist score is 1\n\n\n\n')









