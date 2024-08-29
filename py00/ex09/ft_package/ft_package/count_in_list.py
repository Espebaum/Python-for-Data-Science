def count_in_list(words, c) -> int:
    c_list = [word for word in words if c == word]
    result = len(c_list)
    return result