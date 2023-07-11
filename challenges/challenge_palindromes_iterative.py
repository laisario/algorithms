def is_palindrome_iterative(word):
    if word == '':
        return False
    reversed_word = list(reversed(word))
    normal_word = list(word)
    if normal_word == reversed_word:
        return True
    return False
