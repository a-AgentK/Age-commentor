print("yes=1 no=0")
n =input ("Please enter your name ~~  ")
x =int(input ("Enter your age ~~  "))
if x<=12:
    print("lol you are baby")
elif 12<x<=17:
    print("wow, so you are teenage. XD")
elif 17<x<=25:
    print("You better focus on your Career ")
    z =int(input("Are you Student?  ~~  "))
    if z==1:
        input("which college are you in?  ~~  ")
    else:
        y=int(input ("are you preparing for college entrance exams?  ~~  "))
        if y==1:
            print("Then do your best Dude")
        else:
            print("phadai likhai karo IAS/IPS bano! ")
        
elif 25<x<=65:
    print("you should be married by now,UNKLE/AUNTY JI")
    print("You Should start doing social services")
    z =str(input ("Are you working? ~~  "))
    input ("where you live ~~  ")
    input ("where you work? ~~  ")
    print ("Great job "+ "Best of luck")
print("HAVE A NICE DAY "+ n)
input ("Exit? ~~  ")
