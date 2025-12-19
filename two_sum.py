# Objetivo: Encontrar índices de dos números que sumen el 'target'.

# Enfoque 1: Fuerza Bruta
# Complejidad: O(n^2) - Lento (compara todos contra todos)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
# Prueba
print(two_sum([2, 7, 11, 15], 9))


# Enfoque 2: Optimizado con Diccionario (Hash Map)
# Complejidad: O(n) - Rápido (una sola pasada)
def two_sum_dict(nums, target):
    vistos = {}
    for i, num in enumerate(nums):
        rest = target - num
        if rest in vistos:
            return [vistos[rest], i]
        vistos[num] = i

# Prueba
print(two_sum_dict([2, 7, 11, 15], 9))
