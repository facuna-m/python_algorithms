# Objetivo: Contar cuántas veces aparece cada caracter.

def frequency_counter(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print(frequency_counter("banana"))