
# merge sort

'''  Divide the given array to recusively until with length 1, then 
merge those array as sorted 1 (subarray 1) +middle element + (subarray 2)
 '''


def merge(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        merge(left_array)
        merge(right_array)

        # Merge the sorted subarrays
        # after splitting recusively lets join
        # l=[] ; r=[] ; 
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # Check if any elements are remaining
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

l = [23, 213, 54, 5, 76, 54, 4, 457, 66, 85, 9]
merge(l)
print(l)  # Print the sorted array


# l=[23, 213, 54, 5, 76, 54, 4, 457, 66, 85, 9]
# merge(l)