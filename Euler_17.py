#Euler_Project_on_Python    #by Pukaedr
d001={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
d011={0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
d010={0:'',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
d100={0:'',1:'onehundred',2:'twohundred',3:'threehundred',4:'fourhundred',5:'fivehundred',6:'sixhundred',7:'sevenhundred',8:'eighthundred',9:'ninehundred'}
x=0
sum=0+11 # 0 + one thousand      0 + 11
while x!=1000:
    i = x // 100
    j = x // 10 % 10
    k = x % 10
    x += 1
    if i==0:
        if j==1:
            sum+=len(d011[k])
            print(d011[k])
        else:
            sum+=len(d010[j])
            sum+=len(d001[k])
            print(d010[j],d001[k])
    else:
        sum+=len(d100[i])
        if j==0 and k==0:
            print(d100[i])
            continue
        sum+=3        #  and = 3          one hundred and fifteen
        if j == 1:
            sum += len(d011[k])
            print(d100[i]," and ",d011[k])
        else:
            sum += len(d010[j])
            sum += len(d001[k])
            print(d100[i]," and ",d010[j],d001[k])
print(sum)