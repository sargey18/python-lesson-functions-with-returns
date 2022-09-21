# make a list of 40 random numbers between 1 and 50

# import random
#
# numbers = []
#
# for num in range(40):
#     numbers.append(random.randint(1, 40))
#
# # make a function to see if a number is on that list
#
# def check_number_is_on_list(check_num, list):
#     # how do we check is check_num is in list?
#     if check_num in list:
#         # we need to show where this is in the list (what does .index() do?)
#         index_num = list.index(check_num)
#
#
#
# check_number_is_on_list(11, numbers)
#
# print(numbers)
# print(index_num)

# why are we getting this error?


# step two -------------------------------------------------------------------


# import random
#
# numbers = []
#
# for num in range(40):
#     numbers.append(random.randint(1, 40))
#
#
# # make a function to see if a number is on that list
#
# def check_number_is_on_list(check_num, list):
#     # how do we check is check_num is in list?
#     if check_num in list:
#         # we need to show where this is in the list (what does .index() do?)
#         index_num = list.index(check_num)
#         return index_num
#
#
#
# result = check_number_is_on_list(11, numbers)
#
# print(numbers)
# print(result)

#step three --------------------------------------------------------------------
#what if the number is not in the list
#we now need to write a new function, that returns two numbers
# the numbers before and after our chosen number... that is not in our list

# create the list and the function like before
#
# import random
#
# numbers = []
#
# for num in range(25):
#     numbers.append(random.randint(1, 40))
#
# def find_position_number(chosen_num, list):
#     if chosen_num in list:
#         index_num = list.index(chosen_num)
#         return index_num
#
#
# # make a new function
# def find_nums_before_after(chosen_num, list):
#     # check chosen num is not in the list
#     if chosen_num not in list:
#         # create a copy of the list
#         copy_list = list.copy()
#         # add the chosen number to the new list
#         copy_list.append(chosen_num)
#         # now we need to sort the numbers in order
#         copy_list.sort()
#         # and now we need the index of the chosen number
#         index_num = copy_list.index(chosen_num)
#         # we can now return values jus before and after this one
#         return copy_list[index_num - 1], copy_list[index_num + 1]
#
#
#
#
# first, second = find_nums_before_after(15, numbers)
#
# numbers.sort()
# print(numbers)
#
# print(first, second)
#
# # we get an error here why do we get the error?


# step four -----------------------------------------------------------

# if the number does not exist in the list return the required number
# this stops us from getting the error

import random

numbers = []

for num in range(40):
    numbers.append(random.randint(1, 25))

def find_num(chosen_num, list):
    if chosen_num in list:
        list.sort()
        idx = list.index(chosen_num)
        return idx


def before_after(chosen_num, list):
    # if not in list
    if chosen_num not in list:
        # copy the list
        copy_list = list.copy()
        # add the chosen to the new list
        copy_list.append(chosen_num)
        # sort the list
        copy_list.sort()
        # get the index
        index1 = copy_list.index(chosen_num)
        return copy_list[index1 - 1], copy_list[index1 + 1]

    return chosen_num, chosen_num


result = find_num(11, numbers)

first, second = before_after(11, numbers)

numbers.sort()
print(numbers)

print(first, second)
