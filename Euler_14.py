#Euler_Project_on_Python    #by Pukaedr
x=999999
count=0
i=x
max=0
maxi=0
while x!=10:
    i = x
    count=0
    while i!=1:
        if i%2==0:
            i/=2
            count+=1
        else:
            i=3*i+1
            count+=1
    if count>max:
        max=count
        maxi=x
    x-=1
print(max, " ", maxi)