from partition2 import partition, partition_array as pa
def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        #generate_image(array,pivot_index)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

l1=[34,223,22,31,1,100,50,40,22,72]
print(f'before sorting: {l1}')
quicksort(l1,0,len(l1)-1)
print(f'after sorting: {l1}')
    