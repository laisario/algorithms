def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0 or word == '':
        return False


print(is_palindrome_recursive('aggua', 1, 2))
