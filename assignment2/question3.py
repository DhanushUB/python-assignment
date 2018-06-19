def hidden(num):  # function to convert the numbers to word
    # using dictionary assigning the keys to the given numbers
    code_dict = {6: 'a', 1: 'b', 7: 'd', 4: 'e', 3: 'i', 2: 'l', 9: 'm', 8: 'n', 0: 'o', 5: 't'}
    letters = ""  # letter array is empty
    for value in num:  # for loop to check the each value in the given input and assign the respective key
        letters = letters + code_dict[int(value)]  # assigning the keys from the code_dict
    print("The missing word is: ", letters)  # prints the letters which are converted form code_dict


 # if __name__ == "__main__":  # this tells from where the code has to start. To start the main function score_throws()
def three():  # to get the numbers
    num = input("Enter the number for the missing word: ")  # accepts inputs from the user and stores in num
    hidden(num)  # sends the inputs to function hidden(num)
