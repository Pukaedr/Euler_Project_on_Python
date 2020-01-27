#Euler_Project_on_Python    #by Pukaedr
x=1
Gsum=0
sumx=0
sumk=0
while x<221:
    j=1
    while j<x:
        if x%j==0:
            sumx+=j
        j+=1

    k=1
    while k<sumx:
        if sumx%k==0:
            sumk+=k
        k+=1
    if sumx==sumk:
        print (sumx, sumk)
        sum+=sumk
        sum+=sumx
    x += 1
print(sum)