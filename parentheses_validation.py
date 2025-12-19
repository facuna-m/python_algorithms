# Objetivo: Validar que los paréntesis cierren en el orden correcto (LIFO).

def is_valid(s):
    stack = []
    #Mapa de cierres: la clave es el cierre
    mapa = {")" : "(", "]" :"[", "}" : "{"}

    for char in s:
        if char in mapa:
            if stack:
                top_element = stack.pop()
            else:
                top_element = "#" #valor basura
            if mapa[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack
    
print(is_valid("()[]{}"))
print(is_valid("(]"))
