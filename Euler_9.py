#aa+bb=cc
#a+b+c=1000
#abc-?
a=0
while a<1000:
    b=0
    while b<1000:
        c=0
        while c<1000:
            if a+b+c==1000 and a*a+b*b==c*c and a<b<c:
                print(a)
                print(b)
                print(c)
                print("Ответ: ",a*b*c)
            c+=1
        b+=1
    a+=1
