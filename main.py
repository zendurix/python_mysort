import random
import time

rand_arr = []
# here you can change size of array to be sorted, range of randomizing numbers, and how long should it be repeated
RANDOM_ARRAY_SIZE = 5000
RANDOM_ARRAY_RANGE = 100000
REPEAT = 3

#########################################################


def my_sort(ent_numb):

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

    sort(ent_numb)

######################################################################


def randomizer():
    i = 0
    while i != RANDOM_ARRAY_SIZE:
        rand_arr.append(random.randint(1, RANDOM_ARRAY_RANGE))
        i += 1


def check_sort():
    ii = 0
    while ii != (len(rand_arr)-1):
        if rand_arr[ii+1] < rand_arr[ii]:
            return False
        ii += 1
    return True


counter = 0
while counter != REPEAT:
    randomizer()
    start = time.time()
    my_sort(rand_arr)
    end = time.time()
#    if counter == 3:
#        rand_arr[8] = 9090909090    # uncomment those two lines to see if check_sort works properly
    print(check_sort())
    print(end - start)
    rand_arr = []    # clearing list
    counter += 1



