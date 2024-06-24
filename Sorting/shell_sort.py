
# insertion will compare nearest element , so
# to overcome the disadvantage of insertion we compare the  distance elements -> gap
# gap-5 -> reduce the gap to 1 

# TODO: very important point is that in forward and reverse direction we should swap the elements


def shellSort(arr):
	n = len(arr)
	gap = int(n/2)  # flooe value

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:

		for i in range(gap,n):

			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = arr[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			arr[j] = temp
		gap =int(gap/ 2)


# Driver code to test above
arr =[23, 213, 54, 5, 76, 54, 4, 457, 66, 85, 9]

n = len(arr)
print ("Array before sorting:")
print(arr)

shellSort(arr)

print ("\nArray after sorting:")
print(arr),


