import random
import sort

if __name__ == "__main__" : 
    unsorted_array = []
    for i in range(20) :
        unsorted_array.append( random.randint(0, 1000) )

    print "beforsort:"
    print unsorted_array

    unsorted_array_copy_one =  unsorted_array[:]
    print "quick_sort:" 
    sort.quick_sort(unsorted_array_copy_one, 0, len(unsorted_array_copy_one) - 1 )
    print unsorted_array_copy_one   

    unsorted_array_copy_two =  unsorted_array[:]
    print "bubble_sort:"
    sort.bubble_sort(unsorted_array_copy_two)
    print unsorted_array_copy_two