# binary search

# 1. rescursive method
def bs(l,s,e,toFind):
    m=int((s+e)/2)
    if s<=e:
        if l[m]==toFind:
            print("Element found at ",m)
        elif l[m]<toFind:
            s=m+1
            bs(l,s,e,toFind)
        else:
            e=m-1
            bs(l,s,e,toFind)
    else:
        print("Element not found", toFind)
    
        
l=[ 1,45,88,134,168,200]
s=0
e=len(l)-1
toFind=450
l.sort()
bs(l,s,e,toFind)

# by using while loop
first=s
last =e
search=toFind
nums=l
middle=int(s+e/2)
while first <= last:
    if nums[middle]<search:
        first = middle+1
    elif nums[middle]==search:
        print("\nThe Number Found at Position: " + str(middle+1))
        break
    else:
        last = middle-1
    middle = int((first+last)/2)
if first>last:
    print("\nThe Number is not Found in the List")


