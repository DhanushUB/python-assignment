def one():
    # 1. If you are given three sticks, you may or may not be able to arrange them in a triangle. 
    # For example, if one of the sticks is 12 inches long and the other two are 1‐inch‐long, 
    # you will not be able to get the short sticks to meet in the middle. For any given three 
    # values, there is a simple test to see if it is possible to form a triangle: if any variable is 
    # greater than the sum of the other two, then you cannot form a triangle using the three 
    # values. Otherwise, you can.  

    # a. Write a function named is_triangle that takes three integers as arguments, and that 
    # returns True or False, depending on whether you can or cannot form a triangle from 
    # sticks with the given lengths. 

    # function named is_triangle
    def is_triangle(a, b, c):
        # condition for three values to form a triangle
        if a > (b + c) or b > (a + c) or c > (a + b):
            print('False')
        else:
            print('True')

    # given 3 random values to be sent in to function is_triangle, (3, 4, 5) will give true and (20, 25, 65) be false
    is_triangle(3, 4, 5)
    is_triangle(20, 25, 65)

    # b. Write a function named start_triangle_check that prompts the user to input three 
    # stick lengths, converts them to integers, and uses is_triangle to check whether sticks 
    # with the given lengths can form a triangle.

    # function for collecting the length of the sticks from the user and sending them to function is_triangle
    def start_triangle_check():
        a = int(input("Enter the length of the 1st stick: "))  # to enter 1st length
        b = int(input("Enter the length of the 2nd stick: "))  # to enter 2nd length
        c = int(input("Enter the length of the 3rd stick: "))  # to enter 3rd length
        is_triangle(a, b, c)  # this will send the enter values of a, b and c to function is_triangle

    start_triangle_check()
