#this function takes in a list, adds each element together, and then divides the sum by the length of the list
def avg_num(nums):
    sum = 0
    denom = len(nums)
    for i in range(len(nums)):
        sum = sum + nums[i]
    avg = sum / denom
    return avg

#this function adds the elements in the list together and returns the sum
def sum_num(nums):
    sum = 0
    for i in range(len(nums)):
        sum = sum + nums[i]
    return sum

#this function takes 3 parameters and returns the calculated exponential
def exp_growth(A,k,t):
    e = 2.7
    P = A * e**(k * t)
    return P

#this function takes a list as a parameter and returns the calculated distance
def point_distance(pts):
    d = (((pts[0] - pts[2])**2) + ((pts[1] - pts[3])**2))**(1/2)
    return d

def main():
    avg1 = avg_num([1,3,5,7,9,7])
    print(avg1)

    avg2 = avg_num([11,31,51,71,90])
    print(avg2)

    sum1 = sum_num([1,3,5,7,9,7])
    print(sum1)

    sum2 = sum_num([11,31,51,71,90])
    print(sum2)
    
    #this for loop iterates through the exp_growth function with the 4 values of A defined in the list.
    nums=[10,1400,1000,200]
    for i in range(len(nums)):
        x = exp_growth(nums[i],0.05,10)
        print(x)

    dist1 = point_distance([2,-4,3,3])
    print(dist1)

    dist2 = point_distance([4,5,7,2])
    print(dist2)

main()