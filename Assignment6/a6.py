import math
import random as rn
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


########################
# PROBLEM 1
########################

# INPUT positive integers n and k
# RETURN an integer (result of n choose k as per equation 2 in HW PDF)
def C(n, k):
    if k==0 or k==n:
        return 1
    else:
        return C(n-1,k) + C(n-1,k-1)



# INPUT positive number m
# RETURN integer (the value of B(m) as per equation 4 in the PDF)
def B(m):
    if m ==0:
        return 1
    else:
        x=(1/(m+1))
        return (-1*x)*sum([C(m+1,k)*B(k)for k in range(m)])





########################
# PROBLEM 2
########################

# INPUT path and file name (read the file as per the format of Table-1 (in the PDF) and) retrn the list as per the output format given below
# RETURNS list of tuples [(0,1650), (10,1750),...,(110,6870)] 
# where each tuple correspond to a particular year (year, population in that year)
def get_data(path,name):
    with open("C200-Assignments-pmanolis/" + path + "/" + name) as nfile:
        return [(int(i.split()[0]),int(i.split()[1])) for i in nfile.readlines()]   
        
    
   

data = get_data("Assignment6", "pop.txt")

# INPUT year 0,10,20,...,110
# RETURN model population
# calculate the population it as per equation 16 in the PDF
def pop(year):
    model= 1436.53*((1.01395)**year)
    return model

# INPUT population data
# RETURN total error
# calculate total error as per equation 18 and 19
def error(data): 
    x=0
    for i in data:
        x += (abs(i[1]-pop(i[0]))/i[1])
    tError =100 * x/12
    return tError
     


########################
# PROBLEM 3
########################

# INPUT A string
# OUTPUT boolean (True or False)
def isogram(x):
    lst=list(x)
    for i in lst:
        if lst.count(i)>1:
            return False
    return True      




########################
# PROBLEM 4
########################

# INPUT A string (in hexadecimal format)
# OUTPUT An integer (decimal equivalent of the input string)
def Hex(n):
    dic={"0":0,"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12,"D":13,"E":14,"F":15}
    lst=list(n)
    sum=0
    length=len(lst)
    
    #Reverse List
    for i in range(int(length/2)):
        x=lst[i]
        lst[i] = lst[length-i-1]
        lst[length-i-1]=x

    #Calculate Sum
    for i in lst:
        sum=sum+(dic[i]*(16**lst.index(i)))
    return sum


########################
# PROBLEM 5
########################

# INPUT an integer
# OUTPUT boolean (True or False)
# return True if divisible by 11 otherwise False
def div_11(x): 
    total=0
    string=str(x)
    for i in range(len(string)):
        if i % 2==0:
            total= total-int(string[i])
        else:
            total= total+int(string[i])
    if total>11:
        return div_11(total)
    elif total==11 or total==0 or total==-11 :
        return True
    else: 
        return False





if __name__ == "__main__":

    # print("This is the code file. To see test results, please run 'a6_test.py'")
    # print("Feel free to write your own tests here. The tests you write below will not be graded.")

    ###### Problem 1
    # print(C(1, 0)) # 1
    # print(C(3, 1)) # 3
    # print(C(4, 3)) # 4

    # print(B(1)) # -0.5
    # print(B(2)) # 0.16666666


    ##### Problem 2
    ##### Code to plot the graph for error between true population and 
    # prediction from the model

    # Uncomment the below code to plot the graph for model prediction.
    # make sure to save the plot under the Assignment7 directory

    # total_error = round(error(data),4)
    # t = np.arange(0.0, 120.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, pop(t),'g')
    # for y,p in data:
    #    ax.plot(y,p,'ro--')

    # ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    # title = "Population Growth. Total ave error = %{0}".format(total_error))
    # ax.grid()
    # plt.show()

    
    ##### Problem 3
    #print(isogram("hello")) # False
    #print(isogram("hlo"))   # True
    #print(isogram(""))      # True


    # ##### Problem 4
    #print(Hex("C1")) 
    #print(Hex("7DE"))
    #print(Hex("70D"))


    # ##### Problem 5
    #print(div_11(11))
    #print(div_11(0))  
    #print(div_11(55))
    #print(div_11(56))
    #print(div_11(111))
    pass