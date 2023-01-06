def create_file(name):
    fil=open(name, "x")
    fil.close()

def read_file(name):
    red=open(name, "r")
    str1=str(red.read())
    return str1

def read_file_lines(name):
    tex=open(name, "r")
    lst=[]
    lst=lst+[str(tex.read())]
    return lst

def write_to_file(name, lst):
    big=open(name, "w")
    if(lst==[]):
        print("empty list")
    for i in range(len(lst)):
        big.write(str(lst[i]))
    big.close()
    return big

def append_to_file(name, lst):
    big=open(name, "a")
    if(lst==[]):
        print("empty list")
    for i in range(len(lst)):
        big.write(str(lst[i]))
    big.close()
    return big

def main():
    create_file("bigtext.txt")
    lst=[4,51,65,7]
    write_to_file("bigtext.txt", lst)
    read_file("bigtext.txt")
    read_file_lines("bigtext.txt")
    lst1=[1,2,69]
    append_to_file("bigtext.txt", lst1)