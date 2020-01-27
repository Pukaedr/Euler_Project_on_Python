#Euler_Project_on_Python    #by Pukaedr
x=1
i=0
j=1
while x<1000000:
    i+=x
    x+=1
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count >=500:
        print(i, ' ', count)
        break
    print(i,' ',count)