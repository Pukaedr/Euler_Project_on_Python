#Euler_Project_on_Python    #by Pukaedr
#fibonachi
f1=1
f2=1
n=0
i=2
while n<1000:
	f3=f1+f2
	f1=f2
	f2=f3
	i+=1
	n=len(str(f3))
print(i, " ",f3, " ",n)