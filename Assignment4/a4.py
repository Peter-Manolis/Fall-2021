import math

###########################################################################
# Functions for Problem 1
###########################################################################
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}

def a(dlst):
    [d,m,y]=dlst
    first=(y)-((14-m)/12)
    return first

def b(dlst):
    x= (a(dlst)+ (a(dlst)/4) -(a(dlst)/100) + (a(dlst)/400))
    return math.floor(x)

def c(dlst):
    [d,m,y]=dlst
    return m+(12*((14-m)/12))-2



# INPUT dlst = [d,m,y]
# RETURN day the week that the given date falls on
def day(dlst):
    [d,m,y]=dlst
    day= (d+b(dlst)+(31*((c(dlst))/12)))%7
    for i in week.keys():
        if i == day:
            return week[i]


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    (a,b,c)=t
    disc=b**2-4*a*c
    if disc>=0:
        value1= (-b + math.sqrt(disc))/(2*a) 
        value2= (-b - math.sqrt(disc))/(2*a)
        return (round(value2,2),round(value1,2))
    else:
       real= round((-b/(2*a)),2) 
       imaginary= round(math.sqrt(abs(disc))/(2*a),2)
       return complex(real,imaginary), complex(real,-imaginary)

   



###########################################################################
# Functions for Problem 3
###########################################################################
def inner_prod(v0,v1):
    prod=0
    for i in range(len(v0)):
        prod=prod+ v0[i]*v1[i]
    return prod


def mag(v):
    mag= math.sqrt(inner_prod(v,v))
    return mag

def angle(v0,v1):
    cos= inner_prod(v0,v1)/(mag(v0)*mag(v1))
    cos=math.acos(cos)
    cos=cos* (180/math.pi)
    return round(cos,2)

def match(people):
    
    lst=[]
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            if i!=j:
                lst+=[[people[i],people[j],angle(people[i],people[j])]]
                j+=1
            else:
                i+=1
            
    return lst


def best_match(scores):
    best_score= scores[0][2]
    for i in range (len(scores)):
        if scores[i][2] < best_score:
            best_score=scores[i][2]
            lst1=scores[i][0]
            lst2=scores[i][1]
    return (lst1, lst2, best_score)



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT 
#RETURN 
def intersect(d0,d1):
    if not d0[0]== d1[0]:
        x1=round(((d1[1]-d0[1])/(d0[0]-d1[0])),2)
        y1= round(((d0[0]*x1)+d0[1]),2)
        return x1, y1
    else:
        False


###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message
def mean(lst):
    sum=0
    for i in lst:
        sum +=i
    return round(sum/len(lst),2)

def variance(lst):
    var=0
    for i in lst:
        var=var+((i-mean(lst))**2)
        final=var/len(lst)
    return round(final,2)

def std(lst):
    return round(math.sqrt(variance(lst)),2)

def mean_centered(lst):
    lst1=[]
    for i in lst:
        lst1+= [i-mean(lst)]
    return lst1


###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def equi(s,d):
    s1=s[0]-d[0]
    s2=s[1]-d[1]
    s3=s[2]-d[2]
    supDem=s1,s2,s3
    return q(supDem)
    

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You can uncomment the below print statements to test you code
    but __remember__ to comment them before submitting the final version.

    Note: Do not leave print statements outside the body of the functions.
    All print statements must be commented after you are done testing your
    code and before pushing the final version of your HW.
    """

    # #problem 1
    #print(day([14,2,2000]))
    #print(day([14,2,1963]))
    #print(day([14,2,1972]))

    #problem 2
    #print(q((3,4,2)))
    #print(q((1,3,-4)))
    #print(q((1,-2,-4)))

    # #problem 3
    people0 = [[0,1,1],[1,0,0],[1,1,1]]
    print(match(people0))
    print(best_match(match(people0)))

    people1 = [[0,1,1,0,0,0,1],
               [1,1,0,1,1,1,0],
               [1,0,1,1,0,1,1],
               [1,0,0,1,1,0,0],
               [1,1,1,0,0,1,0]]
    print(best_match(match(people1)))
    #output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #85


    # #problem 4
    # l0 = (2,3)
    # l1 = (-1/2,2)
    # print(intersect(l0,l1)) #-2/5,11/5
    # print(intersect((1,4),(-1/2,1/2)))
 
    #problem 5
    #lst = [1,3,3,2,9,10]

    #print(mean(lst))
    #print(variance(lst))
    #print(std(lst))
    #print(mean(mean_centered(lst)))

    #problem 6
    #s = (-.025,-.5,60)
    #d = (0.02,.6,20)
    #print(equi(s,d))

