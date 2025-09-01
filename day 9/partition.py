def partition(my_list):
    pivot = my_list[-1]
    j=0
    for i in range(1, len(my_list)):
        if my_list[i] < pivot:
            j += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
            j+=1
    my_list[0], my_list[j] = my_list[j], my_list[0]
    
    l1=[34,223,22,31,1,100,50,40,22,72]
    print(f'before partition: {l1}')
    partition_array(l1)
    print(f'after partition: {l1}')
    