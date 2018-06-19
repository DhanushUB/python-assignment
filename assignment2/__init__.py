import assignment2.question1
import assignment2.question2
import assignment2.question3
# to select the option for respective question. Example: 1 for first question, 2 for second question

option = int(input("Enter the question number for assignment 2: "))
if option == 1:
    question1.one()
    exit()
elif option == 2:
    question2.two()
    exit()
elif option == 3:
    question3.three()
    exit()
