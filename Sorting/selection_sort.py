
# selection sort
l=[95, 6, 23, 4, 459, 54, 594, 54, 66, 85, 96]

for i in range(len(l)):
    min=i #considering this as the min element index
    for j in range(i+1,len(l)):
        # itersting rest of the element and checking the minimum and swapping with it
        if l[j]<l[min]:
            min=j
    # after finding the minimum element swapping it
    l[i],l[min]=l[min],l[i]
    print(l)
print(l)

# if swapping element is same -> stable swapping is also there 4 (a) st , 4 (b) nd

# for i in range(len(l)):
#     min=i #considering this as the min element index
#     for j in range(i,len(l)):
#         # itersting rest of the element and checking the minimum and swapping with it
#         if l[j]<l[min]:
#             min=j
#     # after finding the minimum element swapping it
#     key=l[min] 
#     #stable sorting
#     while min>i:
#         l[min]=l[min-1]
#         min-=1
#     l[i]=key 
#     # It's just shifting one position left from key to the i 
#     print(l)
# print(l)