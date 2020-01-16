i=100
j=100
x=0
max=0
while i<1000:
    j=100
    while j<1000:
        x=i*j
        if (x>99999):
            if x//100000==x%10 and x//10000%10==x//10%10 and x//1000%10==x//100%10 and max<x:
                max=x
        else:
            if x//10000==x%10 and x//1000%10==x//10%10 and max<x:
                max=x
        j+=1
    i+=1
print(max)