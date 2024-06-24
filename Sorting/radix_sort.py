

# Radix sort is also called as Bucket Sort

# It's the sorting based on the  digits , you can also perform this for alphabets ,
# It's uses the  counting sort , because of non comparative sorting 



# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
	# counting sort is faster than radix sort


	n = len(arr) 

	# The output array elements that will have sorted arr 
	output = [0] * (n) 

	# initialize count array as 0  because of 0,1,2,3,4,5,6,7,8,9
	count = [0] * (10) 

	# Store count of occurrences in count[] 
	for i in range(0, n): 
        # exp denotes the digit place value like  1, 10, 100, 1000 ,...
		index = (arr[i]/exp1) 
		print(index)
		count[int((index)%10)] += 1

	# Change count[i] so that count[i] now contains actual 
	# position of this digit in output array 
	for i in range(1,10): 
		count[i] += count[i-1] 

	# Build the output array 
	i = n-1
	while i>=0: 
		index = (arr[i]/exp1) 
		output[ count[ int((index)%10) ] - 1] = arr[i] 
		count[int((index)%10)] -= 1
		i -= 1

	# Copying the output array to arr[], 
	# so that arr now contains sorted numbers 
	i = 0
	for i in range(0,len(arr)): 
		arr[i] = output[i] 

# Method to do Radix Sort
def radixSort(arr):

	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1 // exp > 0:
		countingSort(arr,exp)
		exp *= 10
    # or

# in c:
    # for i in range(i=1;max1//exp>0;i*10){
    # }

# Driver code to test above
arr =[23, 213, 54, 5, 76, 54, 4, 457, 66, 85, 9]

radixSort(arr)

for i in range(len(arr)):
	print(arr[i],end=" ")

