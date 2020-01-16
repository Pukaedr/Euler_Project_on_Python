i=100
x=0
while i<1000:
    x=i*i
    if (x>99999):
        if x//100000==x%10 and x//10000%10==x//10%10 and x//1000%10==x//100%10:
            print(x)
    else:
        if x//10000==x%10 and x//1000%10==x//10%10:
            print(x)
    i+=1