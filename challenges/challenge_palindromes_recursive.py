def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    not_reverse = word
    word[::-1]
    if not_reverse == word:
        return True
    return False
    """Faça o código aqui."""
    raise NotImplementedError


print(is_palindrome_recursive('aggua', 1, 2))
