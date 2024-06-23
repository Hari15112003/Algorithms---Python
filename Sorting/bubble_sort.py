
# bubble -sort
l=[23,43,54,54,5,6,54,96,45,66,85]
for i in range(len(l)-1):
    for j in range(0,len(l)-1-i):
        # len(l)-1-i is used to reduce the comparison
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
    print(l)
print(l)
print("bwiih c")

# Reducing the number of passes when sorted
for i in range(len(l)-1):
    toSwap=0
    for j in range(0,len(l)-1-i):
        # len(l)-1-i is used to reduce the comparison
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
            toSwap=1
    if toSwap==0:
        print(l)
        break
print(l)


