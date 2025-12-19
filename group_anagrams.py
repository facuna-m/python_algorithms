# Objetivo: Agrupar palabras que tienen las mismas letras.

def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["roma", "saco", "amor", "cosa", "perro"]))