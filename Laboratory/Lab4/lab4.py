def even_number(lst):
    '''
    Given a list of integer as an input, return a new list contains all integers in lst that are even number.
    
    input:
    lst - a list of integer numbers

    output:
    a new list contains all of the even numbers in the input list. 
    '''
    lst2=[]
    for i in lst:
        if i%2 == 0:
            lst2.append(i)
    return lst2



def star_patern(n):
    '''
    given an integer n, write a function to print the bellow  
    note to do this operation you can't use the .append method for lists

    given n as an input, write a function that prints the bellow pattern:
    for example for n = 5:
    *
    **
    ***
    ****
    *****
    '''
    for i in range(0,n):
        # for j in range(0,i):
        print("*"*(i+1))

    

        


def print_num(n):
    '''
    given an input integer n, print numbers from n to 0 using while loops.

    for example for n = 5:
    5
    4
    3
    2
    1
    0

    input:
    n-integr number
    '''
    while n >= 0:
       print(n)
       n=n-1


def dict_example(dict):
    '''
    we have a dict as an input that contains names of the candidate as a key 
    and the number of votes for that candidate as a value for that key. Please
    return the name of a peson who has the maximum votes.
    example:
    dict = {
        'john': 3
        'mike': 32
        'anna': 34
        'leo': 16
    }

    expected ouput: 'anna'

    '''
    votes=0
    max_votes_name=""
    for key in dict.keys():
        if dict[key] > votes:
            votes=dict[key]
    max_votes_name=key
    return max_votes_name



if __name__ == '__main__':
    # TODO:
    # implement testing
    print(even_number([3, 6, 2, 99, 32]))

    star_patern(5)

    print_num(5)

    dict = {
        'john': 3,
        'mike': 32,
        'anna': 34,
        'leo': 16 }
    print(dict_example(dict))
