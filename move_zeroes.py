# Objetivo: Mover ceros al final sin crear una lista nueva.

def move_zeroes(nums):
    pos = 0
    
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    
    for i in range(pos, len(nums)):
        nums[i] = 0
    
    return nums

print(move_zeroes([0, 1, 0, 3, 12]))