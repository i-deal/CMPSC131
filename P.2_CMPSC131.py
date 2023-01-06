#part 1:

#read the file to a 2d list
def reader(name):
    infile = open(name, "r")
    lst = []
    for line in infile:
        word = line.split("\n")
        word1 = str(word[0]).split(" ")
        lst = lst + [word1]
    infile.close()
    return lst

#helper function, returns whether or not an element has been checked before
def finder(x,lst1):
    y = 0
    for i in range(len(lst1)):
        if(x == lst1[i]):
            y += 1
    return y

#finds all the unique elements in a given 2d list and returns them in a list
def unique(lst):
    lst1 = []
    lst1 += [lst[0][0]]
    for i in range(len(lst)):
        for y in range(len(lst[i])):
            x = finder(lst[i][y],lst1)
            if(x == 0):
                lst1 += [lst[i][y]]
    return lst1

#helper function, adds the line # and word # info that belong to a specific word
def lst_info(lst,x):
    for i in range(len(lst)):
        tmp = lst[i]
        lst[i] = [tmp] + [x+1] + [i+1] #lst[i] =[Word, Line, Word #]

#helper function, finds the total occurrences of a word and rearranges the list into a 2d list
def bake(lst,ulst,i):
    loc = []
    r = 0
    for x in range(len(lst)):
        for y in range(len(lst[x])):
            if(ulst[i] == lst[x][y][0]):
                r += 1
                loc += [lst[x][y][1]] + [lst[x][y][2]]
    tmp = ulst[i]
    ulst[i] = [tmp] + [r]
    for q in range(len(loc)):
        ulst[i] += [loc[q]] #ulst format: 'word', occurrences, line, word#...(line and word# repeat for how many occurrences) 

#transforms the unique elements list into a 2d list with all the necessary information                
def transform_lst(lst,ulst):
    i = 0
    while(i <= (len(lst)-1)):
        lst_info(lst[i],i)
        i += 1
    for i in range(len(ulst)):
        bake(lst,ulst,i)

#helper function, writes the 2d list to the csv file with proper spacing
def rewrite(i,lst,outfile):
    for z in range(len(lst[i])):
        outfile.write(str(lst[i][z]) + ",")
    outfile.write("\n")

#writes the necessary length header and writes the 2d list contents to the csv file
def writer(lst,name):
    head1 = "Words, Occurrences,"
    head2 = "Line, Word #,"
    outfile = open(name, "w")
    r = 0
    for i in range(len(lst)):
        l = (len(lst[i])-2)//2
        if(l > r):
            r = l
    outfile.write(head1+(head2*r)+"\n")
    for i in range(len(lst)):
        rewrite(i,lst,outfile)
    outfile.close()

#part 2:

#prints a map of the key-value pairs, each line is a pair
def entire_map(lst):
    for i in lst:
        for u in range(len(i)):
            print(i[u], ' ', end="")
        print('\n')

#returns the values for a given key and checks if the input is in the list
def get_value(word, y):
    list = []
    for i in range(len(y)):
        if(y[i][0]) == word:
            for u in range(1, len(y[i]), 1):
                list += [y[i][u]]
    if list == []:
        list = -1
    return list

#finds the specified occurence and returns its location
def get_location(word, o, y):
    list = []
    for i in range(len(y)):
        if (y[i][0]) == word and y[i][1] > o:
            for u in range((2+(o-1) *2),(2 + (o * 2)), 1):
                list = list + [y[i][u]]
    if list == []:
        list = [-1, -1]
    return list

#part 3:

#creates a 2d list with length equal to the original, but containing empty lists
def delete_table(olst):
    lst = []
    for i in range(len(olst)):
        z = []
        lst += [z]
    return lst

#helper function, determines whether a given key is in the table or not
def check_key(lst,word):
    x = 0
    for i in lst:
        if i[0] == word:
            x += 1
    return x

#creates a copy of the original list with the specified values removed, checks if the input is valid
def delete_entry(olst,ent):
    lst = []
    for i in range(len(olst)):
        z = []
        if(olst[i][0] != ent):
            for x in range(len(olst[i])):
                z += [olst[i][x]]
            lst += [z]
        else:
            z = [olst[i][0]]
            lst += [z]
    w = check_key(olst,ent)
    if w == 0:
        lst = -1
    return lst

#helper function, finds how many times a given key is repeated in the table
def check_occur(lst,ent):
    occur = 0
    for i in lst:
        if(i[0] == ent):
            occur = i[1]
    return occur

#helper function, creates a copy of the original list with the specified location values removed
def remove_loc(olst,ent,loc):
    lst = []
    for i in range(len(olst)):
        z = []
        if(olst[i][0] != ent):
            for x in range(len(olst[i])):
                z += [olst[i][x]]
            lst += [z]
        else:
            for x in range(0,2*loc,1):
                z += [olst[i][x]]
            for x in range((2*loc)+2,len(olst[i]),1):
                z += [olst[i][x]]
            lst += [z]
    return lst

#checks if the input is valid and removes the specified location from the 2d list
def delete_location(olst,ent,loc):
    gr = check_occur(olst,ent)
    if(gr >= loc):
        lst = remove_loc(olst,ent,loc)
    else:
        lst = -1
    w = check_key(olst,ent)
    if w == 0:
        lst = -1
    return lst

def main():
    x = reader('bigtext.txt')
    y = unique(x)
    transform_lst(x,y)
    entire_map(y)
    val = get_value('Dan', y)
    loc = get_location("Dan", 4, y)
    blank = delete_table(y)
    no_ent = delete_entry(y,'Dan')
    no_loc = delete_location(y,'Dan',1)
    writer(y,'bigtext3.csv')
    
main()