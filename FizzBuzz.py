def fizz_buzz(n):
    my_list = []
    for i in range(1, n+1):
        my_list.append(i)
    for num in my_list:
        # Condición más especifica primero
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz(15)

def fizz_buzz_optimized(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz_optimized(15)