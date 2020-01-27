#Euler_Project_on_Python    #by Pukaedr
#diagonal
x=1
sum=1
flag=0
smesh=1
while x<1002001: 
	x+=1
	x+=smesh
	flag+=1
	sum+=x
	if flag%4==0:
		flag-=4
		smesh+=2
print(sum)