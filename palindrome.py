def is_palindrome(string):
    string_lower = string.lower()
    clear_string = ""

    for char in string_lower:
        if char.isalnum():
            clear_string += char

    inverted_string = clear_string[::-1]
    
    return clear_string == inverted_string

print(is_palindrome("Anita lava la tina"))
print(is_palindrome("Hola Mundo"))
print(is_palindrome("Ana"))

def is_palindrome_pro(string):
    clean = "".join([char.lower() for char in string if char.isalnum()])
    return clean == clean[::-1]


print(is_palindrome_pro("Anita lava la tina"))
print(is_palindrome_pro("Hola Mundo"))
print(is_palindrome_pro("Ana"))