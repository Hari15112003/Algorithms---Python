# insertion sort

a=[23, 13, 54, 5, 76, 54, 4, 457, 66, 85, 96]


# first element is always sorted
# unsorted list / sorted list
for i in range(1,len(a)):
    tmp=a[i] #store the  current element in tmp
    j=i-1 # it have the j-1 goes to sorted index 
    while j>=0 and a[j]>tmp:
        a[j+1]=a[j]
        j-=1
        print(a)
    a[j+1]=tmp
print(a)
