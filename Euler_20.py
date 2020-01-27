#Euler_Project_on_Python    #by Pukaedr
x=1
n=100
for i in range (1,n):
    x*=i+1
sum=0
while x!=0:
    sum+=x%10
    x=x//10
print(sum)