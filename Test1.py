# Talking computer
class Names():
    
    def __init__(self):
        """
        This is the list
        """
        self.names = []


class Ages():
   
    def __init__(self):
        """
        this is the list
        """
        self.ages = []


class Objects():
    def __init__(self):
        self.objects = []


class Passcode():
    def __init__(self):
        self.pas = str(1234)


class Questions():
    def __init__(self):
        self.start_questions = []
        self.next_questions = []
        self.third_questions = []
        self.passcode_question
        self.person
        self.spy

    def start_question(self):
        q = input("what is your name:")
        self.start_questions.append(q)
        return

    def next_question(self):
        q = input("what is your age?")
        self.next_questions.append(q)
        return

    def third_question(self):
        q = input("do you have anything with you?")
        self.third_questions.append(q)
        print("very good now we can get down to buisness")
        return

    def passcode_question(self):
        q = input("Enter the passcode, it must be 4 digits:")
        if q == str(1234):
            print("You are in")
            print()
            print("You have cracked the code!")
            print("")
            print("Now you just have to get past the restrictions!")
            print("First one:")
        else:
            print("you are wrong!")
            Questions().passcode_question()

        

    def person(self):
        q = input("Is anyone with you:")

        if q == 'no' or 'No':
            print("very good you pass!")
        else:
            print("wrong answer!")
            Questions().person()
        return


    def spy(self):
        q = input("Are you a spy:")

        if q == "No" or "no":
            print("very good!")
            print("restriction 2 passed!")
        else:
            print("You can not enter!")
            Questions().spy()


class Instructions():
    def __init__(self):
        self.start_instructions

    def start_instructions(self):
        print("Instructions:")
        print('''\n   Answer everything simpley. With only a "yes"
or "no" unless, asked if you have anything\
 with you or anyone.\n''')
        return
        
class Story(self):
    pass

    def __init__(self):
        pass

    def unlocked_first_part():
        

    
