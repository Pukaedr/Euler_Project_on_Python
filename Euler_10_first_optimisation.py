#Euler_Project_on_Python    #by Pukaedr and Tao
x=10
summa=17
while x<2000000:
        if x%10==0 and x%10==2 and x%10==4 and x%10==5 and x%10==6 and x%10==8:
            x+=1
            continue
        i=2
        flag=0
        while i<x:
            if x%i==0:
                flag=1
                break
            i+=1
        if flag==1:
            x += 1
            continue
        summa+=x
        print(x)
        x+=1
print("Ответ: ",summa)
