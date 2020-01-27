#Euler_Project_on_Python    #by Pukaedr
x=2
sum=0
flag=0
while x<2000000:
    flag=0
    j=2
    while j<x:
        if x%j==0:
            flag=1
        j+=1
    if flag==0:
        sum+=x
        print(x)
    x+=1
print("Ответ: ",sum)