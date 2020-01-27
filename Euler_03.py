#Euler_Project_on_Python    #by Pukaedr
chislo=600851475143
i=4
j=2
otvet=0
flag=0
while i<chislo:
    j=2
    flag=0
    if chislo%i==0:
        while j<i-1:
            if i%j==0:
                flag=1
            j+=1
        if flag==0:
            otvet=i
            print(otvet)
    i+=1
print("ответ ",otvet)