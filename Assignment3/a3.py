import math

#Problem 1

#INPUT n0 start colony size, m growth rate, t time
#RETURN final colony size
def N(n_0, m, t):
    size= n_0*math.exp(m*t)
    return math.ceil(size)

#INPUT t days
#RETURN number of teeth
def N_t(t):
    teeth= 71.8*math.exp(-8.96*math.exp(-.0685*t))
    return math.ceil(teeth)

#INPUT pressures Pi, Pf 
#RETURN work joules
def W(P_i, P_f):
    r=8.314
    t=300
    work=r*t*math.log(P_i/P_f)
    return math.ceil(work)
    

#INPUT V miles per hour, A area, C_l lift coefficient
#RETURN lbs 
def L(V,A,C_l):
    k=.0033
    lbs= k *V**2*A*C_l
    return math.ceil(lbs)

###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN True if discriminant is real, False otherwise
def q(t):
    (a,b,c)=t
    if b**2-(4*a*c) >0:
        return 1
    else:
        return 0


###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT item and list
#RETURN True if item is in the list
#CONSTRAINT You cannot use 'in' -- must use bounded looping
def m(x,lst):
    for i in lst:
        if i==x:
            return True

def amt(r,no_tax):
    sum=0
    
    for i in r:
        if not m(i[0],no_tax):
            sum= sum + (i[1]*1.07)
        else:
            sum=sum+ i[1]
    return round(sum,2)

###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT p0 = (x0,y0) p1 = (x1,y1)
#RETURN (a,b,c) for line ax + by + c = 0
def f(p0,p1):
    (x0,y0)=p0
    (x1,y1)=p1
    if x0!=x1:
        m= (y1-y0)/(x1-x0)
        b= y0-(m*x0)
        return (m,b)
    else:
        return ()



###########################################################################
# Functions for Problem 5
###########################################################################
#INPUT List of numbers
#RETURN Various means or error message

err_msg = ["Data Error: 0 values", "Data Error: 0 in data"]

def arithmetic_mean(nlst):
    
    sum1=0
    if len(nlst)>0:

        for i in range(0, len(nlst)):
            sum1= sum1 + nlst[i]
        return sum1/(len(nlst))
    else:
        return err_msg[0]

def geo_mean(nlst):
    sum2 = 0 
    if len(nlst)>0:

        for i in range(0, len(nlst)):
            sum2=sum2+ math.log10(nlst[i])
        return 10**(sum2/len(nlst))
    else:
        return err_msg[0]

def har_mean(nlst):
    buttom=0
    mean=0
    if len(nlst)>0:
        
        for i in range(0,len(nlst)):
            if nlst[i]!=0:
                buttom= buttom + (1/(nlst[i]))
            else:
                return err_msg[1]
        mean=len(nlst)/buttom
        return mean
    else:
        return err_msg[0]    
def RMS_mean(nlst):
    sum3=0
    mean=0
    if len(nlst)>0:
        
        for i in range(0,len(nlst)):
            sum3=sum3 + (nlst[i]**2) 
        mean= math.sqrt(sum3/len(nlst))
        return mean
    else:
        return err_msg[0]
    

###########################################################################
# Functions for Problem 6
###########################################################################
#INPUT x filters
#RETURN fixed cost
def F(x):
    return 10000

#INPUT x filters
#RETURN variable cost
def V(x):
    if x>=0 and x<=40000:
        vari=-.0001*x**2+10*x
        return vari
#INPUT x filters
#RETURN total cost
def C(x):
    return V(x)+F(x)

###########################################################################
# Functions for Problem 7
###########################################################################

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN montly payment float
def Mortgage(house):
    (p,i,n)=house
    decimal= (i/100)/12
    monthly= p*((decimal*(1+decimal)**(n*12))/((1+decimal)**(n*12)-1))
    return round(monthly,2)

#INPUT list [p,i,n] principal, interest rate, payments
#RETURN the difference between total payout and value
#of home 
#REQUIRES Mortgage function
def total_paid(house):
    (p,i,n)= house
    return (Mortgage(house)*n*12)-p


###########################################################################
# Functions for Problem 8
###########################################################################
#INPUT list of numbers
#RETURN True if geometric series, False otherwise
def is_geo(xlst):
    is_geo= 1
    x0,x1=xlst[0],xlst[1]
    if len(xlst) >2:

        for i in range(2,len(xlst)):
            x2=xlst[i]
            if ((x1/x0) or (x1*x0)) != ((x2/x1) or (x2*x1)):
                is_geo=0
                break
            x0,x1=x1,x2
        return is_geo
    else:
        return 0

if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """
    # #problem 1
    #print(N(500,100,4)) 
    #print(N_t(1000))
    #print(W(10,1))
    #print(L(33.8,512,0.515))

    #problem 2
    #print(q((1,4,-21)))
    #print(q((3,6,10)))
    #print(q((1,0,-4)))

    #problem 3
    receipt = [[1,1.45],[3,10.00],[2,1.45],[5,2.00]]
    no_tax = [33,5,2]
    print(amt(receipt,no_tax))

    # #problem 4
    # print(f((2,3),(6,4)))
    # print(f((1,6),(3,2)))
    # print(f((1,3),(1,5)))
 
    #problem 5
    #print(arithmetic_mean([1,2,3]))
    #print(geo_mean([2,4,8]))
    #print(har_mean([1,2,3]))
    #print(RMS_mean([1,3,4,5,7]))

    #problem 6
    #print(C(0))
    #print(C(100))
    #print(C(1000))

    #problem 7
    #house = [300000,2.9,30]
    #print(Mortgage(house))
    #print(total_paid(house))

    # #problem 8
    #xlst = [1/2,1/4,1/8,1/16,1/32]
    #print(is_geo(xlst))
    #xlst = [1,-3,9,-27]
    #print(is_geo(xlst))
    #xlst = [625,125,25]
    #print(is_geo(xlst))
    #xlst = [1/2,1/4,1/8,1/16,1/31]
    #print(is_geo(xlst))
    #xlst = [1,-3,9,-26]
    #print(is_geo(xlst))
    #xlst = [625,125,24]
    #print(is_geo(xlst))
    #print(is_geo([1/2,1/4]))