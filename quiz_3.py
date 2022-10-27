x=input("enter a word," )
def char(x):
    u=0
    l=0
    for i in x:
        if i>="a" and i<="z":
          l+=1
        if i>="A" and i<="Z":
         u+=1
    print("lower case letter in word",l)
    print("upper case letter in word",u)
char(x)
