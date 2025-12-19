# Objetivo: Detectar si hay repetidos.
# Estrategia: Los Sets (conjuntos) eliminan duplicados automáticamente.

def contains_duplicate(list):
    no_dup = set(list)
    if len(no_dup) == len(list):
        return False
    else:
        return True
    
print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))

# Versión simplificada (One-Liner)
def contains_duplicate_one_line(list):
    return len(set(list)) != len(list)

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))