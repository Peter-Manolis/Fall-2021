import math
import random as rn
from tkinter import N


########################
# PROBLEM 1
########################

#INPUT positive number n
#RETURN log of number base 2
def log_2(n):
    if n >0:
        return math.log(n,2)

#INPUT list of immutable objects
#RETURN list of probability distribution
def makeProbability(xlst):
    dic={}
    probList=[]
    for i in xlst:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]=dic[i]+1
    for i in dic:
        probList+=[(dic[i]/len(xlst))]
    return probList







#INPUT probability distribution
#RETURN non-negative number entropy
# You CANNOT use count()
def entropy(xlst):
    # Step 1: Get the probability of each element
    # Step 2: Get summation of entropy function
    # Step 3: Round summation to 2 decimal places
    xlst=makeProbability(xlst)
    tropy=0
    for i in xlst:
        tropy+=i*log_2(i)
    return round(-tropy,2)





########################
# PROBLEM 2
########################

#INPUT list of 0s 1s
#OUTPUT longest list of 1s
def L(x):
    count=0
    biggest=0
    for i in x:
        if i ==1:
            count+=1
            if biggest < count:
                biggest=count
        else:
            count=0
    return biggest





########################
# PROBLEM 3
########################

#INPUT non-negative integer
#OUTPUT True if divisible by 9, False otherwise
# You CANNOT use modulus (%) AND you CANNOT directly divide by 9
def div_9(x):
    total=0
    string=str(x)
    for i in range(len(string)):
        total= total+int(string[i])
    if total>9:
        return div_9(total)
    elif total==9 or total==0 :
        return True
    else: 
        return False






########################
# PROBLEM 4
########################

#INPUT set of recurrence equations
#OUTPUT implement recursively, tail recursive generator
def p(n):
    if n ==0:
        return 10000
    else:
        return p(n-1)+.02*p(n-1)
def p_t(n,v=0):
    pass
    #Skipped as it is tail recursion

def p_g():
    n=10000
    while True:
        yield n
        n = n+.02*n



def c(n):
    if n ==1:
        return 9
    else:
        return (9*(c(n-1)))+ 10**(n-1) - (c(n-1))

def c_t(n,v=0):
    pass
    #Skipped as it is tail recursion


def c_g():
    n=9
    e=1
    while True:
        yield n
        n=(9*n) + (10**e) - n
        e=e+1




def d(n):
    if n==0:
        return 1
    else:
        return 3*d(n-1)+1

def d_t(n,v=1):
    pass
    #Skipped as it is tail recursion


def d_g():
    n=1
    while True:
        yield n
        n=(3*n)+1




########################
# PROBLEM 5
########################

#INPUT list of numbers
#OUTPUT list sorted ascending using potato-smith

#INPUT list of numbers
#OUTPUT return sorted ascending
def insertion(a):
    i=1 
    while i < len(a):
        j=i
        while j>0:
            if a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
            j-=1
        i+=1
    return a

#INPUT list of numbers
#OUTPUT sorted list ascending using potato and insertion
def potato(x):
    size =2
    lst=[]
    while size<len(x):
        lst=[]
        for i in range(0,len(x),size):
            lst += insertion(x[i:i + size])
        size=size*2
    lst=insertion(lst[0:])
    return (lst)
    
    
    





########################
# PROBLEM 6
########################

#INPUT list of numbers
#OUTPUT  [a,b,c] where:
#    a = start index
#    b = end index
#    c = maximal sum of these indices
# You may use sum(list)
# Be cautious to use sum correctly - don't use it as a variable. It's a built-in function name.
def msi(x):
    max=0
    for i in range(0,len(x)+1):
        for j in range(0,len(x)+1):
            if sum(x[i:j])>max:
                max=sum(x[i:j])
                a=i
                b=j
    return [a,b,max]
        






########################
# PROBLEM 7
########################

#INPUT positive number w/ two decimal places
#OUTPUT [q,d,n,p] which is the minimal amount of coins needed
def dollars(x):
    lst=[0,0,0,0]
    i=x
    while i>0:
        if x >= .25:
            lst[0]+=1
            x=round(x-.25,2)
        elif x >=.10:
            lst[1]+=1
            x=round(x-.10,2)
        elif x >=.05:
            lst[2]+=1
            x=round(x-.05,2)
        elif x >=.01:
            lst[3]+=1
            x=round(x-.01,2)
        else:
            return lst





if __name__ == "__main__":
#     # Feel free to add your own tests here to help with error handling. 
#     print("This is the code file. To see test results, please run 'test_a5.py'")
#     print("Feel free to write your own tests here. The tests you write below will not be graded.")

    # #Problem 1
    #s0 = ["a", "b", "a", "c", "c", "a"]
    #print(makeProbability(s0))
    #print(entropy(s0))
 
    # #Problem  2
    #x = [0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    #print(L(x))
    #y=[1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1]
    #print(L(y))

    # #Problem 3
    #xlst = [99,0,18273645,22,27]
    #for i in xlst:
    #    print(div_9(i))

    # Problem 4
    #for i,j in zip(range(10),p_g()):
    #    print(i,p(i),p_t(i),j)
    '''
    0 10000 10000 10000
    1 10200.0 10200.0 10200.0
    2 10404.0 10404.0 10404.0
    3 10612.08 10612.08 10612.08
    4 10824.3216 10824.3216 10824.3216
    5 11040.808031999999 11040.808031999999 11040.808031999999
    6 11261.62419264 11261.62419264 11261.62419264
    7 11486.8566764928 11486.8566764928 11486.8566764928
    8 11716.593810022656 11716.593810022656 11716.593810022656
    9 11950.925686223109 11950.925686223109 11950.925686223109
    '''
    #for i,j in zip(range(1,10),c_g()):
    #     print(i,c(i),c_t(i),j)
    '''
    1 9 9 9
    2 82 82 82
    3 756 756 756
    4 7048 7048 7048
    5 66384 66384 66384      
    6 631072 631072 631072   
    7 6048576 6048576 6048576
    8 58388608 58388608 58388608
    9 567108864 567108864 567108864
    '''
    #for i,j in zip(range(10),d_g()):
    #     print(i,d(i),d_t(i),j)
    '''
    0 1 1 1
    1 4 4 4
    2 13 13 13      
    3 40 40 40      
    4 121 121 121   
    5 364 364 364   
    6 1093 1093 1093
    7 3280 3280 3280
    8 9841 9841 9841
    9 29524 29524 29524
    '''
    #Problem 5
    #lst = [rn.randint(0,100) for _ in range(rn.randint(1,20))]
    #print(lst)
    #print(potato(lst))
    
    
    #Problem 6

    #x = [7, -9, 5, 10, -9, 6, 9, 3, 3, 9]
    #data = [(-1)**rn.randint(0,1)*rn.randint(1,10) for _ in range(10)]
    #print(msi(x))
    #print(data)
    #print(msi(data))

    #Problem 7
    xlt = [2.24,1.19,4.16,1.01,1.10,2.00]
    for i in xlt:
        print(dollars(i))
