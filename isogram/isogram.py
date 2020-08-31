def is_isogram(string):
    chars = set()
    for char in str.lower(string).replace(' ', '').replace('-', ''):
        if char in chars:
            return False
        else:
            chars.add(char)
    return True
