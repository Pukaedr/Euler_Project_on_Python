i=1
j=2
fibo=0
summa=2
while fibo<4000000:
    fibo=j+i
    if fibo>4000000:
        break
    if fibo%2==0:
        summa+=fibo
    i=j
    j=fibo
print(summa)