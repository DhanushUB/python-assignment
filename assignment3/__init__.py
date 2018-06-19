import assignment3.question1
import assignment3.question2
# to select the option for respective question. Example: 1 for first question, 2 for second question

option = int(input("Enter the question number for assignment 3: "))
if option == 1:
    question1.one()
    exit()
elif option == 2:
    question2.two()
    exit()
