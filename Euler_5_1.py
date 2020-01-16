x=20
flag=0
while flag==0:
    i=2
    flag2=0
    while i<20:
        if x%i!=0:
            flag2=1
        i+=1
    if flag2==1:
        flag=0
        print(x)
    x+=1