


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

