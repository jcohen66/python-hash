def hash_function_simple1(text):
    return sum(ord(character) for character in text)

# Everything is treated as a str
def hash_function_str(key):
    return sum(ord(character) for character in str(key))

# Strings are distinguishable from numbers by encasing key in quotes.
def hash_function_repr(key):
    return sum(ord(character) for character in repr(key))

# Remove anagrams by taking into account position in key.
# Enumerate from 1 to avoid multiply by zero.
def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    )

# Remove anagrams by taking into account position in key.
# Enumerate from 1 to avoid multiply by zero.
# Slow and always results in even hash bc of symmetric quotes.
def hash_function_symmetric(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    )

# Remove the left quote if exists to avoid always even hash.
def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
    )
