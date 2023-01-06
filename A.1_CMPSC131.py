#Problem-1
def count_repeat(lst,tmp):
    r=0
    for i in range(len(lst)):
        if(tmp==(lst[i])):
            r=r+1
    return r

def most_com(lst):
    lst2=[] #this list stores a list that stores how many times an element in lst is repeated
    lst3=[] #this list stores which elements are most and least repeated
    lar=0
    #this loop iterates through lst
    for i in range(len(lst)):
        tmp=lst[i]
        #this function iterates through lst again, returning how many times tmp is repeated
        repeats=count_repeat(lst,tmp)
        lst2=lst2+[repeats]
    #this loop iterates through lst2 and returns the most and least repeated element
    sml=lst2[0]
    for i in range(len(lst2)):
        if(lst2[i]>lar):
            lar=lst2[i]
            most=lst[i]
        elif(lst2[i]<=sml):
            sml=lst2[i]
            least=lst[i]
    lst3=lst3+[most]+[least]
    return lst3

#Problem-2
def window(lst,x,w):
    tmp=0
    for i in range(x,x+w,1):
        if(lst[i]>tmp):
            tmp=lst[i]
    return tmp

def slide(lst,w):
    lst2=[]
    for i in range(len(lst)-(w-1)):
        x=window(lst,i,w)
        lst2=lst2+[x]
    print(lst2)

def main():
    lst1=[10,30,60,88,10,30,10,60,3,88]
    x=most_com(lst1)
    print(x)

    lst2=[2,5,12,3,4]
    slide(lst1,2)

main()