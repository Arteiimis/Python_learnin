s=['-','+']
sum=0
for i in range(1,101):
    sum=sum+(eval(s[i%2]+'i'))
print(sum)
