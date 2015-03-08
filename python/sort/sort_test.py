import random
import sort


array = []
for i in range(20) :
	array.append( random.randint(0, 1000) )

print "beforsort:"
print array

print "quick_sort:"	
sort.quick_sort(array, 0, len(array) - 1 )
print array	

print "bubble_sort:"
sort.bubble_sort(array)
print array