# Reutilización de frequency_counter.py
def frequency_counter(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def are_anagrams(word1, word2):
    return frequency_counter(word1) == frequency_counter(word2)

print(are_anagrams("roma", "amor"))
print(are_anagrams("casa", "saco"))