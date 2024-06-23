
# linear search
# It's also called as Sequential Search

l=[ 2,31,4,543,5435,435,3453400]
toFind=4355
k=0
for i in range(len(l)):
    if l[i]==toFind:
        print(i)
        k=1 
        break
if k==0:
    print("Element not found",toFind)
