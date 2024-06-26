"""
One of the code implementations for the problems in Lab3.py

I may add some more interesting functions such as append_prime_number
"""

# List Operations

def manual_append(list_one, element):
    '''
    given a list and an element append the element to the list 
    note to do this operation you can't use the .append method for lists

    inputs:
    list_one - a list of values can be any type
    element - a value of any type

    output:
    one coherent list of all elements combined

    '''
    return list_one + [element]


def manual_remove(list_one, val):
    '''
    given a list and a specific value remove the item and report wether you were successful 
    by using a for loop to iterate over the list

    inputs:
    list_one - list of specific type(int or str) 
    val - the value that you want removed

    output:
    list - the list with the element removed if the element is not found return the list
    '''
    output=[]
    for item in list_one:
        if item!=val:
            output=manual_append(output,item)
    
    return output

# Doing things with list data structures

def compare_lists(list_one, list_two):
    '''
    given 2 lists compare and report which indexes are different in an output list

    your output should look something like this: [1, 3, 5]
    
    which means that index 1, 3, and 5 are different values these lists can compare any data type

    inputs:
    list_one - list of a specific type (int or str) of length n
    list_two - list of a specific type (int or str) of length n

    outputs:
    list of ints which correlate to indexes that are different in a list
    '''
    output = []
    for elm_i in range(len(list_one)):
        if list_one[elm_i]!= list_two[elm_i]:
            output= manual_append(output,elm_i)

    return output


def factorial_for(n):
    '''
    given a number calculate the factorial value using a for loop

    input:
    n - integer value that will be factorial you want to calculate 

    output:
    the calculated factorial of the input value 
    '''
    output=1
    for num in range(n,0,-1):
        output*=num

    return output
if __name__ == '__main__':
    list1=[1,2,3,4,"a",5,6]
    list2=[11,12,13,14,5,16,17]
    element="cat"
    output_manual_append=manual_append(list1,element)
    print(output_manual_append)
    
    print(manual_remove(list1,4))
    #print(manual_remove(list1,100))
    #print(manual_remove(list1,0))

    print(compare_lists(list1,list2))

    print (factorial_for(5))
    #print (factorial_for(0))
