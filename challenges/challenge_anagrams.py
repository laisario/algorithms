def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ('', '', False) 
    first_array = list(first_string.lower())
    second_array = list(second_string.lower())
    
    order(first_array, 0, len(first_string) - 1)
    order(second_array, 0, len(second_string) - 1)

    firstStringOrder = ''.join(first_array)
    secondStringOrder = ''.join(second_array)

    if (firstStringOrder == secondStringOrder):
        anagram = True
    else:
        anagram = False
 
    
    return (firstStringOrder, secondStringOrder, anagram)


def order(letters, first_index, last_index):
    if first_index < last_index:
        d = division(letters, first_index, last_index) 
        order(letters, first_index, d - 1)
        order(letters, d + 1, last_index)


def division(letters, first_index, last_index):
    last_letter = letters[last_index]
    delimiter = first_index - 1

    for index in range(first_index, last_index):
        if letters[index] <= last_letter:
          delimiter = delimiter + 1
          currLetter = letters[index]
          letters[index] = letters[delimiter]
          letters[delimiter] = currLetter

    letters[delimiter + 1], letters[last_index] = letters[last_index], letters[delimiter + 1]

    return delimiter + 1
