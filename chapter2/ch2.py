def add(xs,y):
    s={"key":y}
    if xs==[]:
       xs=[str(s)]
       return xs
    p=[[xs[-1]]+[str(s)]]
    xs= xs + p
    return xs
#####################################################
def g():
    lst=[]
    #################################################################################33
    def f(xs):
        answer1=input(" Operation Successful,What do you want to do now?.\n1.Add data.\n2.Show the current list.\n3.Quit.\n") 
        if answer1=="1":
           g2 = int(input("What do you want to add?"))
           xs=add(xs,g2)
           print("************")
           print(xs)
           print("************")
           return f(xs)
        if answer1=="2":
            print("************")
            return xs
        if answer1=="3":
            a="************\nUntil next time bye.\n************"
            return a
        return "************\nPlease select the correct option.\n************"
    ##############################################################
    if answer=="1":
       g1 =int(input("What do you want to add?"))
       lst=add(lst,g1)
       print("************")
       print(lst)
       print("************")
       return f(lst)
    if answer=="2":
        print("************")
        return lst
    
    if answer=="3":
        a="************\nUntil next time bye.\n************"
        return a
    return "************\nPlease select the correct option.\n************"
answer= input("Hi,I am TUI, What do you want to do?\n1.Add data.\n2.Show the current list.\n3.Quit.\n")
print(g())


