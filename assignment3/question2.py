# deepcopy: a copy of one object is copied into another. It is not to reflect any changes made to another copy
# of object
from copy import deepcopy


def two():

    def run_mail_boxes(row, column):  # value is received from the function initialize
        mail_boxes = []  # initialising an empty array
        mail_boxes.append(['c'] * column)  # insertion of 'c' into boxes as per the number of columns

        for r in range(1, row):  # for loop to take action with respect to number of rows
            mail_boxes.append(deepcopy(mail_boxes[r-1]))  # any changes in mail_boxes will not affect the previous copy
            for c in range(0, column):  # for every element in column starting from 0
                if (c + 1) % (r + 1) == 0:  # if modulo of c+1 and r+1 is zero and
                    if c >= r:  # if c greater or equal to r
                        if mail_boxes[r][c].lower() == 'o':  # if value mail_boxes for respective c and r is lower 'o' then
                            mail_boxes[r][c] = 'C'  # changes value in mail_boxes for respective c and r to 'C'
                        elif mail_boxes[r][c].lower() == 'c':  # else if value in mail_boxes for respective c and r is 'c'
                            mail_boxes[r][c] = 'O'  # then, change value in mail_boxes for respective c and r will be to 'O'
                elif (c + 1) % (r + 1) != 0:  # else if, modulo of c+1 and r+1 is not equal to zero
                    # then any change value in mail_box for respective r and c to lower
                    mail_boxes[r][c] = mail_boxes[r][c].lower()
        # to print all the columns
        for c in mail_boxes:
            print(c)

    def initialize():  # function to accept the number of rows and columns
        row = int(input("Enter number of rows: "))
        column = int(input("Enter number of columns: "))
        run_mail_boxes(row, column)  # pushes the values to the function run_mail_boxes

    initialize()

