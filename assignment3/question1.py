def one():
    def word_count(directory_name, file_name):  # function to accept the file form the directory
        file_name = directory_name+"\\"+file_name  # storing the file into file_name
        try:  # for try doing the below and throw error if any
            with open(file_name, 'r') as file:  # to open the file using with open and read it(performed by 'r'.
                data = file.read()  # stores the read file into data
                words = data.split()  # splits the whole string in single words
                counts = dict()  # using dictionary, empty
                for word in words:  # loop for each element in words
                    if word in counts:  # if the word is in the dictionary the increase its count by 1, every time its finds the word in the file
                        counts[word][0] += 1
                    else:
                        counts[word] = [1, len(word)]  # else the count if the word will remain as count 1, also collects the length of the word

                occurence_file = open(directory_name+"\\output1.txt", 'w')  # creates a text file for output1 (occurences of the word)
                length_file = open(directory_name+"\\output2.txt", 'w')  # creates a text file for output2 (length of the word)

                for c in counts:  # for every element in counts
                    occurence_line = str(c)+" - "+str(counts[c][0])+"\n" # stores the count of number of times a word as repeated
                    length_line = str(c)+" - "+str(counts[c][1])+"\n"  # stores the length of all the words
                    occurence_file.write(occurence_line) # writes the values stored in occurence_line to output1 via occurence_line
                    length_file.write(length_line)  # writes the values stored in length_line to output 2 via length_file

                occurence_file.close()  # closes the output1 file
                length_file.close()  # closes the output2 file

        except IOError: # for any input/output error, example, if path to the file is not defined correctly.
            print("Error reading input file, please check the file")  # prints the error message
    # sends the values to function word_count
    word_count("C:\\Users\\Dhanush Mahesala\\Desktop\\New folder (2)\\Python\\Assignments\\Assignment3","File_to_be_read.txt")