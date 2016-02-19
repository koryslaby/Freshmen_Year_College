from Test1 import Questions

from Test1 import Names

from Test1 import Ages

from Test1 import Objects

from Test1 import Instructions


q1 = Questions()
list_of_names = Names()
list_of_ages = Ages()
list_of_objects = Objects()
instr = Instructions()


instr.start_instructions()
q1.start_question()
q1.next_question()
q1.third_question()


print(q1.start_questions)
print(q1.next_questions)
print(q1.third_questions)

q1.passcode_question()
q1.person()
q1.spy()
