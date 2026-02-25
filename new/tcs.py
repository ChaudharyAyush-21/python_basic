#1. Move all zeroes to the end of the array while maintaining the order of non-zero elements.

# def moveZeroes(arr):
#     non_zero_index = 0
#     for a in arr:
#         if a!= 0:
#             arr[non_zero_index] = a
#             non_zero_index += 1
#     for i in range(non_zero_index, len(arr)):
#         arr[i] = 0
#     return arr

# arr = [4,5,0,1,9,0,5,0]

# print(moveZeroes(arr))

#2. WRITE THE PROGRAM FOR FIBONACCI
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# terms = int(input("Enter number of terms: "))
# for i in range(terms+1):
#     print(fibonacci(i), end=" ")

#3. Count the number of even and odd numbers in an array.
# def even_odd(arr):
#     count_even = 0
#     count_odd = 0
#     for a in arr:
#         if a%2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     return count_even, count_odd

# arr = [1,2,3,4,5,6,7,8,9]
# print(even_odd(arr))

#4. POWER OF THE NUMBER
# def power(x, n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 1 / power(x, -n)
#     elif n % 2 == 0:
#         half_power = power(x, n // 2)
#         return half_power * half_power
#     else:
#         return x * power(x, n - 1)
    
# x = 2
# n = -3
# print(power(x, n))

#5. THE NUMBER IS ARMSTRONG NUMBER OR NOT
# def is_armstrong(n):
#     total = 0
#     digits = len(str(n))   # count digits
    
#     for digit in str(n):
#         total += int(digit) ** digits
    
#     return total == n


# 
# print(is_armstrong(153))  # True
# print(is_armstrong(123))  # False

# THE NUMBER IS PRIME OR NOT
# n= int(input("Enter a number: "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(f"{n} is a prime number.")
# else:
#     print(f"{n} is not a prime number.")










