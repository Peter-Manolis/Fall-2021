###########################
# Problem One
###########################
# There is no unit testing 
# for this problem
###########################
import matplotlib.pyplot as plt
import random as rn
import math
import numpy as np

# translates a random int into a step along the random walk
# parameters: int i for the step index, numpy array x for tracking the left/right location at index i,
# numpy array y for tracking the forward/backward location at index i
# return: none
def step(x,y,i):
    
    # We have already setup the below line to return a list of four values
    # [1,2,3,4] out of which you will select the actions and act accordingly.
    # i.e., if you select 1 from direction below then move right and so on for other values.
    direction = rn.randint(1,4)
    # TODO: implement this function
    if i ==0:
        x[0],y[0]=0,0
    else:
        if direction==1:
            x[i]=x[i-1]+1
            y[i]=y[i-1]
        elif direction==2:
            x[i]=x[i-1]-1
            y[i]=y[i-1]
        elif direction==3:
            y[i]=y[i-1]+1
            x[i]=x[i-1]
        elif direction==4:
            y[i]=y[i-1]-1
            x[i]=x[i-1]


# do not change code below for graphit() function.
# this function actually draws the plot that you see in the
# PDF. Your plot will be different from the one given in the 
# PDF due to the randomness in the walk.
def graphit(x,y,n):
   
    plt.title("Random {0} Walk\nLast Location {1},{2}".format(n,int(x[n-1]),int(y[n-1])) )
    plt.plot(x,y) 
    plt.plot([x[1],x[1]],[y[1]-10,y[1]+10], "b-")
    plt.plot([x[1]-10,x[1]+10],[y[1],y[1]], "b-")
    plt.plot([x[n-1]-10,x[n-1]+10],[y[n-1],y[n-1]], "r-")
    plt.plot([x[n-1],x[n-1]],[y[n-1]-10,y[n-1]+10], "r-")
    plt.show() 




###########################
# Problem Two
###########################

# input: 2 points in 2-dimensions example (1,2) or (3,4)
# output: the distance between them
def distance(p1, p2):
    a=(p1[0]-p2[0])**2
    b=(p1[1]-p2[1])**2
    return math.sqrt(a+b)

# input:  list of pairs, where each pair is a point in 2-dimensions
# output: [point1, point2, distane] where distance is the minimum out of all possible pair of points in xlst
# point1 is first point
# point2 is second point
# distance is the distance between the points
def brute(xlst):
    a=()
    b=()
    xdistance=distance(xlst[0],xlst[1])
    for i in range(len(xlst)):
        for j in range(i+1,len(xlst)):
            if distance(xlst[i],xlst[j]) <xdistance:
                xdistance=distance(xlst[i],xlst[j])
                a=xlst[i]
                b=xlst[j]
    return [a,b,xdistance]





###########################
# Problem Three
###########################

# input: N and time (set to 40)
# output: calculated productivity value

def productivity(N, T = 40):
    return N*T*(.55-.00005*N*(N-1))

""" 
Do Not Change the functions below.
All you have to do is to complete the productivity function above
The below functions are used to create the plot as shown in the PDF.
"""
def fp(f):
    h = .00001
    return lambda x: (f(x + h) - f(x-h))/(2*h)

def newton(f, fp, x, tau):
    def n(x):
        while f(x) > tau:
            x = x - f(x)/fp(x)
        return x
    return n(x)




###############
# PROBLEM Four
###############
# You CANNOT use ANY modules in this problem
###############

# input: a list of elements
# ouptut: a list of lists, where each sublist is a permutation of the original input list
def permutation(lst):
    if len(lst) == 1:
        return [lst]
    lst2 = []
    for i in range(len(lst)): 
        nums = permutation(lst[:i] + lst[i+1:]) 
        for j in nums:
            lst2.append([lst[i], *j])
    return lst2









###############
# PROBLEM Five
###############

class Vector:
    def __init__(self, *x):
        self.__v = x

    def get_tuple(self):
        return self.__v

    def __add__(self,other):
        return Vector(*(self.__v[i]+other.__v[i] for i in range(len(self.__v))))


    def __sub__(self,other):
        return Vector(*(self.__v[i]-other.__v[i] for i in range(len(self.__v))))


    def __rmul__(self,other):
        return Vector(*(i*other for i in self.__v))

    def __mul__(self,other):
        return Vector(*(self.__v[i]*other.__v[i] for i in range(len(self.__v))))


    def __abs__(self):
        return math.sqrt(sum([i**2 for i in self.__v]))

    def __neg__(self):
        return Vector(*(-1*i if i>0 else i for i in self.__v))

    def __eq__(self, other):
        return len(self.__v)==sum([self.__v[i]==other.__v[i]for i in range(len(self.__v))])

    def __repr__(self):
        return ('<'+str(self.__v).strip('()')+'>')




if __name__ == "__main__":

    # You are free to uncomment the below statements to test the code
    # but comment them back before submitting your final work.

# #PROBLEM 1
    #number of steps
    # n = 100000   #You should change the number of steps to see
                #to see how it affects the plot
    # x = np.zeros(n) 
    # y = np.zeros(n) 

    #fill array with step values 
    # for i in range(1,n):
        # step(x,y,i)

    # graphit(x,y,n)

##PROBLEM 2

    # x = [(rn.randint(1,50), rn.randint(1,50)) for _ in range(10)]
    # print(x)
    # print(brute(x))

##PROBLEM 3
    # f = fp(productivity)
    # x = math.ceil(newton(f,fp(f),62,.01))
    # y = math.ceil(productivity(x))
 
    # print("The maximum productivity is P({0}) ~ {1} person x hrs".format(x,y))

    # t = np.arange(0.0, 100.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, productivity(t),'g')
    # ax.plot(x,productivity(x), 'bo--')
    # ax.set(xlabel ="Number of people", ylabel="person x hrs", title = "Maximal Productivity P({0}) ~ {1}".format(x,y))

    # ax.grid()
    # plt.show()

## PROBLEM 4
    #print(permutation([1,2,3]))
    #print(permutation([1,2,3,4]))


## PROBLEM 5       
    x,y,w = Vector(1,2),Vector(3,-1),Vector(*(10,10))  
    z,a = Vector(0,3,2),Vector(-1,-1,-1) 
    print(x,y,z,a)
    print(x+y,z+a)
    print(x*y,z*a)
    print(5*x,5*z)
    print(abs(x),abs(z))
    print(-x,-z)
    print(x - y + y == x, 2 * z == z + z)

    pass