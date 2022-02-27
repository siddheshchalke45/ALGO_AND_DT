import math


# BRUTE FORCE SOLUTION

def search(list_numbers, number_to_search):
    for i in range(len(list_numbers)):
        if list_numbers[i] == number_to_search:
            return i
    
    ## number is not present in the list
    return -1



print('Requested number is present at ' + str(search([1,2,3,4,5,6,7,8,9], 1)) + ' index')
print('Requested number is present at ' + str(search([1,2,3,4,5,6,7,8,9], 9)) + ' index')
print('Requested number is present at ' + str(search([1,2,3,4,5,6,7,8,9], 5)) + ' index')
print('Requested number is present at ' + str(search([1,2,3,4,5,6,7,8,9], 11)) + ' index')
print('Requested number is present at ' + str(search([], 1)) + ' index')


# BINARY SEARCH (List must be sorted in some order. In our case it is ascending order.)

def binary_search(list_numbers, start_index, end_index,number_to_search):
    
    if len(list_numbers) == 0:
        return -1
    
    if start_index == end_index:
        if list_numbers[start_index] == number_to_search:
            return start_index
        else:
            return -1

    center_index_of_list = math.ceil((start_index + end_index)/2)

    if list_numbers[center_index_of_list] == number_to_search:
        return center_index_of_list
    elif list_numbers[center_index_of_list] > number_to_search:
        return binary_search(list_numbers, start_index, center_index_of_list - 1, number_to_search)
    else:
        return binary_search(list_numbers, center_index_of_list + 1, end_index, number_to_search)




print(str(binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 1)))
print(str(binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 11)))

print(str(binary_search([0], 0, 0, 0)))
print(str(binary_search([0], 0, 0, 1)))

print(str(binary_search([], 0, 0, 11)))

print(str(binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 5)))
print(str(binary_search([0,1,2,3,4,5,6,7,8,9], 0, 9, 9)))
print(str(binary_search([0,1,2,3,4,5,6,7,8], 0, 8, 5)))
print(str(binary_search([0,1,2,3,4,5,6,7,8], 0, 8, 8)))