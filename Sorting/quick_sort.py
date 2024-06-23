

# quick sort

# 3 preior conditions  to remember

# 1.intially i=p=0 ; j=len(arr)-1  ( any element can be as pivot element)
#  Major condition is that all the elements less than pivot is in left side and greater than  right side 
# 
# [ partion 1 , pivot (proper place always ) , partion2]
# again do it for partion


# easy approach by using list -comprehension
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p=arr[0]
        l= [i  for i in arr[1:] if i<=p ]
        r=[i  for i in arr[1:] if i>p ]
        return quicksort(l)+[p]+quicksort(r)  #using recursion here


l=[23, 213, 54, 5, 76, 54, 4, 457, 66, 85, 9]
# print(quicksort(l))


# s,p=0,0  # starting ->element as pivot element
# e=len(l)
# if l[s]<=l[p]:
#     s+=1
# elif l[e]>l[p]:
#     e-=1
# if i<j:
#     swap() => element of i and j
# if i>j:
#     swap pivot & j

    
 



