# this function takes two float or integer paramaters and returns their average
def avg_num(x,y):
    a = (x+y)/2
    return a

# call avg_num function and save it to a variable
avg = avg_num(2,4)

# this function takes a string as a parameter and prints it
def print_str(s):
    print(s)

# call print_str function
print_str("testing testing 1... 2... 3...")

# this function takes no parameters, but stores a local variable and returns it
def my_num():
    f = 68
    return f

# call fav_num function and save it to a variable
fav_num = my_num()

# this function stores a string as a local variable and prints it
def hello_msg():
    print("Hello World")

# call hello_msg function
hello_msg()

# this function takes three parameters and returns the calculated exponential growth using them
def exp_growth(A,k,t):
    e = 2.7
    P = A * e**(k * t)
    return P

# this function takes four parameters and return the calculated distance using them
def point_distance(x1,y1,x2,y2):
    d = (((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)
    return d

# this function takes four parameters and returns the calculated slope using them
def slope(x1,y1,x2,y2):  
    m = (y2 - y1) / (x2 - x1)
    return m

# main function to invoke the exp_growth, point_distance, and slope functions
def main():
    pop1 = exp_growth(10000,.05,10)
    print("Population #1: ", pop1) 

    pop2 = exp_growth(140000,.07,25)
    print("Population #2: ", pop2)
     
    dist1 = point_distance(2,3,-4,3)
    print("Distance #1: ", dist1)

    dist2 = point_distance(4,7,5,2)
    print("Distance #2: ", dist2)
    
    slo1 = slope(2,3,-4,3)
    print("Slope #1: ", slo1)

    slo2 = slope(4,7,5,2)
    print("Slope #2: ", slo2)

main()

