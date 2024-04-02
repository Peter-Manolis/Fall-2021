import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()




def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("C200-Assignments-pmanolis/Laboratory/Lab8//blank.txt", "r") as some_file:
        some_file =  open("C200-Assignments-pmanolis/Laboratory/Lab8//blank.txt","r")
        contents=some_file.read()
        return contents

def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("C200-Assignments-pmanolis/Laboratory/Lab8/blank.txt","r") as some_file:
        open("C200-Assignments-pmanolis/Laboratory/Lab8/blank.txt","r")
        contents=some_file.readlines()
        return contents


def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    stuff=["a","b", "c", "d", "e", "f"]
    with open("C200-Assignments-pmanolis/Laboratory/Lab8/wrong.txt","w") as file_to_write:
        for s in stuff:
            file_to_write.write(s+"\n")



def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("C200-Assignments-pmanolis/Laboratory/Lab8/wrong.txt","a")  as file_to_write:
        for s in range(4):
            file_to_write.write(str(s)+"\n")




def FileIO_example(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    count=0
    #reading
    with open("C200-Assignments-pmanolis/Laboratory/Lab8/blank.txt","r")as some_file:
        original_contents=some_file.read()
    #split lines
    split_line= original_contents.split("\n")
    
    good_lines=[]
    #count lines
    for line in split_line:
        splitted_words=line.split(" ")
        if len(splitted_words) <=5:
            count+=1
        else:
            good_lines.append(line.strip())

    #write lines
    with open("C200-Assignments-pmanolis/Laboratory/Lab8/blank.txt","w") as towrite:
        for line in good_lines:
            towrite.write(line)
            towrite("\n")

    return count



def calculation(filePath):
    '''
    Given a file path, we want to open the file, read each line. in each line we have a number
    we want to calculate the summation of numbers in last 2 lines and write the sum at the end of the 
    file we read from it. (eah time that we run this function we add one number of fibonacci series to the file)
    '''
    pass


if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example("Laboratory/Lab8/testing.data", "Laboratory/Lab8/clean.txt")))

    calculation("Laboratory/Lab8/calculation.txt")