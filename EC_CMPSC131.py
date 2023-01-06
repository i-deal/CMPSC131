def a_list():
    mylst=[1,2,3,4,5,6,7,8,9]

    print("using iterator")
    for i in mylst:
        print(i, end=" ")
    print()
    
    print("using index")
    for i in range(len(mylst)):
        print(mylst[i], end=" ")
    print()
    mylst2=[]
    for j in range(len(mylst)):
        mylst2=mylst2+[mylst[j]]
    
    print("mylst:", mylst)
    print("mylst2:", mylst2)

def a_2d_list_1():
    mylst=[[1,2,3],[4,5,6],[7,8,9]]

    print("using iterator")
    for i in mylst:
        print(i, end=" ")
    print()
    
    print("\nusing index")
    x=1
    for i in range(len(mylst)):
        print("x:", x, mylst[i], end=" ")
        x=x+1

def a_2d_list_2():
    mylst=[[1,2,3],[4,5,6],[7,8,9]]
    length=len(mylst)
    print("length:", length)
    
    print("using iterator")
    for i in mylst:
        for j in i:
            print(j, end=" ")
        print()

    print("using range function")    
    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[x][y], end=" ")
        print()

def a_2d_list_3():
    mylst=[[1,2,3],[4,5,6],[7,8,9]]
    mylst2=[]

    print("using range function")    
    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[x][y], end=" ")
            mylst2=mylst2+[mylst[x][y]]
        print()
    
    print("mylst2 formed!") 
    print("mylst2:", mylst2)

def static_list_creation():
    mylst=[[0 for x in range(5)] for y in range(5)]
    for x in range(len(mylst)):
        for y in range(len(mylst[x])):
            print(mylst[x][y], end=" ")
        print()

def a_2d_list_4():
    mylst=[[1,2,3],[4,5,6],[7,8,9]]
    mylst2=[]

    print("using range function")    
    for x in range(len(mylst)):
        mylst3=[]
        for y in range(len(mylst[x])):
            mylst3=mylst3+[mylst[x][y]]
        mylst2=mylst2+[mylst3]
    
    print("mylst2:", mylst2)

def read_data_from_function():
    fptr=open("bigtext.txt", "r")
    str=fptr.readline()
    print(str)
    lst=str.split(",")
    print(lst)
    x=int(lst[2])
    y=x+1
    print("x:", x,"y:", y)

read_data_from_function()