numberlist = [3,5,6,7,9,12,15,18,23,24,26,38,59,64,83]
number_to_find = 15
def binnary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index+right_index)//2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index+1

        else:
            right_index = mid_index-1

    return -1

print(f'index of the number is: {binnary_search(numberlist, number_to_find)}')

