#this function swaps elements in a given list, this is a supporting function
def swap_val(lst,x,y):
    tmp=lst[x]
    lst[x]=lst[y]
    lst[y]=tmp

#this function finds the largest element in the list and returns it, this is a supporting function
def find_largest(lst):
    tmp=lst[0]
    for i in range(len(lst)):
        if(lst[i]>tmp):
            tmp=lst[i]
    return tmp

#this function finds the smallest element in the list and swaps it to the current index, this is a supporting function
def swap_least(lst,x,l):
    tmp_low=l
    for i in range(x,len(lst),1):
        if(lst[i]<tmp_low):
            tmp_low=lst[i]
            tmp_i=i
    swap_val(lst,tmp_i,x)

#this function finds the largest element in the list and swaps it to the current index, this is a supporting function
def sortr(lst):
    for i in range(len(lst)-1):
        for i in range(len(lst)-1):
            if(lst[i]<lst[i+1]):
                swap_val(lst,i,i+1)

#this function uses the process outlined in the L.5 instructions to sort the given list in ascending order and return it
def ascender(lst):
    l=find_largest(lst)
    for i in range(len(lst)-1):
        swap_least(lst,i,l)
    return lst
    
#this function sorts a given list in descending order by comparing each element to the next and swapping the values if it is smaller
def descender(lst):
    cop_lst=[]
    for i in range(len(lst)):
        cop_lst=cop_lst+[lst[i]]
    for i in range(len(cop_lst)):
        sortr(cop_lst)
    print(cop_lst)

def main():
    lst1=[7,2,6,1,5,3,4,9,8,300]
    lst2=[1,10,3,3,15,6,0,-19]
    x=ascender(lst1)
    print(x)
    descender(lst2)

main()