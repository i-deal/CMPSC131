#TypeError, a certain type of variable cannot be used with another type of variable

#this function will causea type error because you cannot add an integrer to a string, to fix it I would replace the code with 
#print('number', num1)
def typer1():
    num1=6
    x='number: '+num1
    print(x)

#this function will return a type error because a list index cannot be a float number, to fix this 
#I will replace the value of x with an integer
def typer2(lst):
    x=0.4
    print(lst[x])
    
#ValueError, the variable type of the input is correct, but the function cannot handle the value

#this function will return a value error as the integer function cannot accept a string, to fix this I will set x to a float
def valer1():
    x='a'
    return int(x)

#this function will return a value error as the float function cannot accept a string, to fix this I will set x to a integer
def valer2():
    x='x'
    print(float(x))

#NameError, an operation uses a variable that has not been assigned a value yet

#this function will return a name error because x has not been assigned yet, to fix this I will assign x a value
def namer1():
    print(x)

#this function will return a name error because even though I passed "lst1" in main to the function, the function renamed it to lst.
#to fix this I will edit the return statement to return lst[0]
def namer2(lst):
    return lst1[0]

#IndexError, this error occurs when a operation calls a list at an index that is greater than the range of the list

#this function will return an index error because 9 is greater than the range of the list, to fix I will use an index inside the range
def inder1(lst):
    print(lst[9])

#this function will return an index error because the length of the lst is 1 greater than the range of the list,
#to fix this I will set x = len(lst)-1
def inder2(lst):
    x=len(lst)
    return lst[x]

def main():
    lst=[1,2,3]
    typer1()
    typer2(lst)
    valer1()
    valer2()
    namer1()
    namer2(lst)
    inder1(lst)
    inder2(lst)

main()