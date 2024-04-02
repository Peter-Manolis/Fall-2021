from calendar import c
import math
from operator import truediv

#problem 1
#input real
#return real
def g(x):
    if x ==0:
        return 1
    else:
        return x+2
 


#problem 2
#input year 1977-1997
#return percent income or "error: year" if year 
#is outside range
def f(t):
    
    if t >=1977 and t<=1984:
        percent= ((2/7)*(t-1977))+12
        return percent 
    elif t>1984 and  t<=1987:
        percent= (t-1977)+7
        return percent 
    elif t>1987 and t<=1997:
        percent= ((3/5)*(t-1977))+11
        return percent 
    else:
        return "error: yeah"




#problem 3
#input t years = 0
#output dollars
def h_0(t):
    cost= 110/(((1/2)*t)+1)
    return cost

def h_1(t):
    cost= 26*((1/4)*t**2-1)**2+52
    return cost 

def h(t):
    return h_0(t)-h_1(t)


#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    import math
    (a,b,c)=coefficients
    value1= (-b + math.sqrt(b**2-4*a*c))/(2*a) 
    value2= (-b - math.sqrt(b**2-4*a*c))/(2*a)  
    return (value1,value2)


#problem 5
#input [arg1,op,arg2,ans]
#output arg1 op arg2 == ans
def eq(lst):
    [arg1,op,arg2,ans] = lst
    if op == "+":
        ans1= arg1 +arg2
    elif op == "-":
        ans1=arg1-arg2
    elif op == "/":
        ans1=arg1/arg2
    elif op == "*":
        ans1=arg1*arg2
    if ans==ans1:
        return True
    else:
        return False
        
        
#problem 6
#input list of swithes
#output True if path from start to end
def path(lst):
    [s0,s1,s2,s3,s4]=lst
    if s0==1:
        if s1==1 and s2==0:
            if s3 ==1 or s4 ==1:
                return True
            else:
                return False
            
        elif s1==0 or 1:
            if s2==1:
                return True
            else: 
                return False
    else:
        return False

#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if x > y:
        return x
    else: 
        return y

#INPUT 3 numbers
#RETURN maximum of the three
#You must use your max2D function
def max3d(x,y,z):
    max= max2d(x,max2d(y,z))
    return max

#from homework
def m(x,y):
    return (x > y)*x + (x <= y)*y

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    #problem 1 
    #print(g(0))
    #print(g(1))
    #print(g(1.01))

    #problem 2
    #print(f(1976))
    #print(f(1977))
    #print(f(1985))
    #print(f(1988))
    #print(f(2000))

    #problem 3
    #print(h(0))
    #print(h(1))
    #print(h(2))

    #problem 4
    #print(q((1,0,-1)))
    #print(q((6,-1,-35)))
    #print(q((1,-7,-7)))

    #problem 5
    #print(eq([14, "/",2, 7]))
    #print(eq([20, "*",19, 381]))
    #print(eq([20, "*",19, 380]))

    #problem 6
    # print(path([1,0,1,0,0]))
    # print(path([1,1,1,0,0]))
    # print(path([1,0,0,1,0]))

    #problem 7
    # print(max3d(1,2,3))
    # print(max3d(1,3,2))
    # print(max3d(3,2,1))