def two():
    # 2. You have just recently been hired to calculate scores for a Dart Board game! Write a function scoreThrows() 
    # that accepts any number of  radius  (can be integers), and returns a total score using the below specification. 
    # Scoring specifications: 
    # 0 points ‐ radius above 10 
    # 5 points ‐ radius between 5 and 10 inclusive 
    # 10 points ‐ radius less than 5 
    # If all radiuses are less than 5, award 100 BONUS POINTS! 
    # An empty input should return 0

    def score_throws():  # function to accept number of chances and to enter the radius.
        radii = []  # empty array to insert the radii
        chances = int(input("Enter the number of chances: "))  # accept number of chances
        # loop to get radius for each chances and store it in array radii.
        for i in range(chances):
            radius = input("Enter the radius:")
            if len(radius) > 0:
                radii.append(int(radius))
        print(radii)  # print the array
        run_program(radii)  # send the radii values to function run_program

    def run_program(radii):  # function to check if the array is empty or not
        if empty_radii(radii):  # if array is empty then go to function empty_radii
            exit()

        print_scores(radii)  # if array is not empty then go to function print_scores

    def empty_radii(radii):  # if the array is empty
        if not radii:  # checks if radii array is empty, not radii mean True value and array is empty
            print("Score: 0")  # prints score is zero

        return not radii  # returns True value

    def print_scores(radii):  # function to check if the bonus points applies or not
        scores = []  # array to store score values
        bonus = True  # setting the bonus value to true
        # Get scores
        for radius in radii:
            scores.append(get_score(radius))

        # Check for bonus
        for radius in radii:
            if radius > 5:
                bonus = False
                break

        print("Score : ", sum(scores))
        if bonus:  # if the bonus applies, sum the scores and add 100 as bonus
            print("Additional bonus of 100 for accuracy, final score: ", sum(scores) + 100)

        return True

    def get_score(radius):  # function to check the radius and classify into the given score specifications
        if radius > 10:  # if the radius is more than 10 then returns the score as 0
            return 0
        if radius >= 5 and radius <= 10:  # if the radius is more than 5 and less than 10 inclusive then returns 5
            return 5
        if radius < 5:  # if the radius is less than 5 then returns the score as 10
            return 10

    # if __name__ == "__main__":  # this tells from where the code has to start. To start the main function score_throws()
    score_throws()