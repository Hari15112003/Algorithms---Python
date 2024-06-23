

#  counting sort is based upon counting distinct digits and  

l=[ 8,3,1,6,7,0,3,6,8,2,6,9,1,8,1,9,4,8,4,3,4,5,9, ]
# counting value will not work for negative values
# to normalize  subtract the oppsite value of -5 -> +5 in each and at result subtract it again

# len(l)=23  which is that position
#  max element is 0-9 which is 10 

count =[0]*(10)
# [0,0,0,0,0,0,0,0,0,0]

result =[0]* len(l)

for i in range(len(l)):
    # updating the count of each l[i] to 0-9
    count[l[i]]+=1
print(count)

# next updating the count with the actual position (position is always index+1)

for i in range(1,10):
    # updating the position means index of the element
    count[i]=count[i]+count[i-1]
print(count)

# to maintain the stability perform sorting from the last array

for i in range(len(l)-1,-1,-1):
    #  or len(l) -> not maintaing the stability
    count[l[i]]-=1
    result[count[l[i]]]=l[i]
print(result)






