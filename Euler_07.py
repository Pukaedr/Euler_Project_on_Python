#Euler_Project_on_Python    #by Pukaedr
x=2
count=0
flag=0
while x!=-1:
    flag=0
    j=2
    while j<x:
        if x%j==0:
            flag=1
        j+=1
    if flag==0:
        count+=1
        print(count)
    if count==10001:
        print("ответ ",x)
        x=-2
    x+=1