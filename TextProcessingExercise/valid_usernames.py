def valid_length(name):
    if 3 <= len(name) <= 16:
        return True
    return False

def valid_chars(name):
    for char in name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True

def no_redundant(name):
    if ' ' in name:
        return False
    return True

def username_is_valid(name: str):
    if valid_chars(name) and valid_length(name) and no_redundant(name):
        return True
    return False

usernames = input().split(', ')
for username in usernames:
    if username_is_valid(username):
        print(username)