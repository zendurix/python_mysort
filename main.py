

def input_numbers():
    x = int
    while x != 0:
        x = int(input())
        ent_numb.append(x)


def max_numb(array):
    arr_i = 0
    maximum = array[0]
    maximum_index = 0

    while arr_i < len(array):
        if array[arr_i] >= maximum:
            maximum = array[arr_i]
            maximum_index = arr_i
        arr_i += 1
    return maximum_index


def sort(sort_arr):

    arr_length = len(sort_arr)
    i = 1
    for something in sort_arr:
        if (arr_length - i) != 0:
            ind = max_numb(sort_arr[0:(arr_length - i + 1)])
            a = sort_arr[arr_length - i]
            sort_arr[arr_length - i] = sort_arr[ind]
            sort_arr[ind] = a
            i += 1

    return sort_arr


ent_numb = []
input_numbers()

sorted_arr = sort(ent_numb)
for x in sorted_arr:
    print(x)

