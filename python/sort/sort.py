def quick_sort(array, begin, end) :
    if begin >= end :
        return
    low = begin
    high = end
    key = array[low]
    while low < high :
        while low < high and array[high] <= key :
            high -= 1
        array[low] = array[high]

        while low < high and array[low] >= key :
            low += 1
        array[high] = array[low]

        array[low] = key

        quick_sort(array, begin, low - 1)
        quick_sort(array, low + 1, end)

		
def bubble_sort(array) :
	for i in range(len(array)-1, 0, -1):
		for j in range(i):
			if array[j] < array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]
			
        
