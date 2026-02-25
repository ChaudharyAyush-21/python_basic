# # printing the pattern
# def print_pattern(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end=" ")
        
#         print()  # Move to the next line after each row

# n= int(input("Enter the number of rows: "))
# print_pattern(n)  # Call the function to print the pattern 


# def print_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1, i+1):
#             print("*", end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# print_pattern(n)  # Call the function to print the pattern 

# def print_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1, i+1):
#             print(j, end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# print_pattern(n)  # Call the function to print the pattern

# def print_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1, i+1):
#             print(i, end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# print_pattern(n)  

# def print_pattern(n):
#     for i in range(1,n+1):
#         for j in range(0,n-i+1):
#             print("*", end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# print_pattern(n)  

# def print_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,n-i+2):
#             print(j, end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# print_pattern(n) 

# def print_pattern1(n):
#     for i in range(n):
#         # space
#         for j in range(0,n-i-1):
#             print(" ", end=" ")
#         # stars
#         for j in range(0,2*i+1):
#             print("*", end=" ")
#         # space
#         for j in range(0,n-i-1):
#             print(" ", end=" ")
#         print()

# # n= int(input("Enter the number of rows: "))
# # print_pattern1(n)  

# def print_pattern2(n):
#     for i in range(n):
#         # space
#         for j in range(0,i):
#             print(" ", end=" ")
#         # stars
#         for j in range(0,2*n-(2*i+1)):
#             print("*", end=" ")
#         # space
#         for j in range(0,i):
#             print(" ", end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# # print_pattern1(n)  
# print_pattern2(n) 

# def print_pattern1(n):
   
#     for i in range(1,2*n):
#         star = i  
#         if i > n:
#             star = 2*n - i
#     # stars
#         for j in range(1, star + 1):
#             print("*", end=" ")
#         print()  # Move to the next line after each row


# n= int(input("Enter the number of rows: "))
# print_pattern1(n)

# def print_pattern1(n):
#     # start = 1
#     for i in range(1,n+1):
#         start = 1
#         if i % 2 == 0:
#             start = 0
#         else:
#             start = 1        
#     # stars
#         for j in range(1,i+1):
#             print(start, end=" ")
#             start = 1 - start
#         print()  # Move to the next line after each row


# n= int(input("Enter the number of rows: "))
# print_pattern1(n)

# def print_pattern2(n):
#     space = 2*(n-1)
#     for i in range(1,n+1):
#         # star
#         for j in range(1,i+1):
#             print(j, end=" ")
#         # space
#         for j in range(1,space+1):
#             print(" ", end=" ")
#         # star
#         for j in range(i,0,-1):
#             print(j, end=" ")
#         print()
#         space -= 2

# n= int(input("Enter the number of rows: "))
# print_pattern2(n) 

# def print_pattern2(n):
    
#     for i in range(1,n+1):
#         # star
#         for j in range(1,i+1):
#             print(j, end=" ")
#         # space
#         for j in range(1,2*n-(2*i-1)):
#             print(" ", end=" ")
#         # star
#         for j in range(i,0,-1):
#             print(j, end=" ")
#         print()
        

# n= int(input("Enter the number of rows: "))
# print_pattern2(n) 

def print_pattern2(n):
    start = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(start, end=" ")
            start +=1
        print()
        
n= int(input("Enter the number of rows: "))
print_pattern2(n) 

# def print_char_pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(chr(ord('A') + j - 1), end=" ")
#         print()

# n = int(input("Enter the number of rows: "))
# print_char_pattern(n)

# def print_char_pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, n - i + 2):
#             print(chr(ord('A') + j -1), end=" ")
#         print()

# n = int(input("Enter the number of rows: "))
# print_char_pattern(n)

# def print_char_pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, i+1):
#             print(chr(ord('A') + i -1), end=" ")
#         print()

# n = int(input("Enter the number of rows: "))
# print_char_pattern(n)

# def print_pattern2(n):
#     for i in range(n):
#         # space
#         for j in range(0, n - i - 1):
#             print(" ", end=" ")
#         # characters
#         ch = ord('A')
#         breakpoint = i
#         for j in range(0, 2 * i + 1):
#             print(chr(ch), end=" ")
#             if j < breakpoint:
#                 ch += 1
#             else:
#                 ch -= 1
#         # space
#         for j in range(0, n - i - 1):
#             print(" ", end=" ")
#         print()

# n= int(input("Enter the number of rows: "))
# print_pattern2(n)  

# def print_pattern2(n):
#     for i in range(1,n+1):

        
#         for j in range(i, 0 ,-1):
#             print(chr(ord('E')-j+1), end=" ")
            
#         print()


# n= int(input("Enter the number of rows: "))
# print_pattern2(n)  

# def print_pattern2(n):
#     inis = 0
#     for i in range(0,n):
#         # star
#         for j in range(1,n-i+1):
#             print("*", end=" ")
#         # space
#         for j in range(0,inis):
#             print(" ", end=" ")
#         # star
#         for j in range(1,n-i+1):
#             print("*", end=" ")
#         inis += 2
#         print()
#     inis1 = 8
#     for i in range(1,n+1):
#         # star
#         for j in range(1,i+1):
#             print("*", end=" ")
#         # space
#         for j in range(0,inis1):
#             print(" ", end=" ")
#         # star
#         for j in range(1,i+1):
#             print("*", end=" ")
#         inis1 -= 2
#         print()
       

# n= int(input("Enter the number of rows: "))
# print_pattern2(n) 

# def print_pattern2(n):
#     spaces = 2*n - 2
#     for i in range(1,2*n):
#         stars = i
#         if i > n:
#             stars = 2*n - i
#         # star
#         for j in range(1,stars+1):
#             print("*", end=" ")
#         # space
#         for j in range(1,spaces+1):
#             print(" ", end=" ")
#         # star
#         for j in range(1,stars+1):
#             print("*", end=" ")
#         if i < n:
#             spaces -= 2
#         else:
#             spaces += 2
#         print()

       

# n= int(input("Enter the number of rows: "))
# print_pattern2(n) 

# def print_pattern2(n):

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if j == 1 or j == n or i == 1 or i == n:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()  
# n= int(input("Enter the number of rows: "))
# print_pattern2(n) 

# def print_pattern2(n):

#     for i in range(0,2*n-1):
#         for j in range(0,2*n-1):
#             top = i
#             bottom = (2*n - 2)-i
#             left = j
#             right = (2*n - 2)-j
            
#             print((n - min(min(top, bottom), min( left, right))), end=" ")
#         print()  
# n= int(input("Enter the number of rows: "))
# print_pattern2(n) 



# square = [x**2 for x in nums]
# square = map(lambda x:x**2 ,nums)
# print(sorted(square))

# def pointer():
#     l = 0
#     r = len(square)-1
#     new = []
#     while l<=r:        
#         if square[l] < square[r] :
#             new.append(square[r])
#             r-=1
#         else:
#             new.append(square[l])
#             l+=1
        
#     return new


# nums = [-4,-1,0,3,10]
# square = [x**2 for x in nums]
# print(square)
# print(pointer())

# def pointer():
#     l = 0
#     r = len(nums)-1
#     new = []
#     while l<=r:        
#         if abs(nums[l]) < abs(nums[r]) :
#             new.append(nums[r]**2)
#             r-=1
#         else:
#             new.append(nums[l]**2)
#             l+=1
#     new.reverse()   
#     return new


# nums = [-4,-1,0,3,10]

# print(pointer())

# [1,2,3,0,0,0,2,5,6]
# def pointer():
#     l = 0
#     r = len(num1)-1
#     result = []
#     while l<r:        
#         if num3[l] < num3[r] :
#             result.append(num3[r])
#             r-=1
#         else:
#             result.append(num3[l])
#             l+=1
      
#     return result


# num1 = [1,2,3,0,0,0]
# num2 = [2,5,6]


# print(pointer())


# # Fibonacci using loop
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# Fibonacci using recursion
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# terms = int(input("Enter number of terms: "))
# for i in range(terms):
#     print(fibonacci(i), end=" ")

# Factorial using loop
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print("Factorial:", fact)

# Factorial using recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# num = int(input("Enter a number: "))
# print("Factorial:", factorial(num))

# PALINDROME
# n = int(input("Enter a number: "))
# rev = 0
# curr = n
# while n>0:
#     k = n % 10
#     rev = rev * 10 + k
#     n = n // 10

# if curr != 0 and rev == curr:
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")



# Palindrome check
# text = input("Enter a string or number: ")
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# Palindrome using recursion
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     return s[0] == s[-1] and is_palindrome(s[1:-1])

# s = input("Enter a string or number: ")
# print("Palindrome" if is_palindrome(s) else "Not Palindrome")


# Reverse number using loop
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print("Reversed number:", rev)

# Reverse number using recursion
# def reverse_number(num, rev=0):
#     if num == 0:
#         return rev
#     return reverse_number(num // 10, rev * 10 + num % 10)

# n = int(input("Enter a number: "))
# print("Reversed number:", reverse_number(n))

# Prime check using loop
# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")

arr = [3, 1, 7, 2, 9, -4, 5]

# Assume first element is min and max
# min_val = arr[0]
# max_val = arr[0]

# for num in arr:
#     if num < min_val:
#         min_val = num
#     if num > max_val:
#         max_val = num

# print("Minimum value:", min_val)
# print("Maximum value:", max_val)

# # TRAVERSAL
# arr = [10, 20, 30]
# for i in range(len(arr)):
#     print(arr[i])

# # INSERTIONN
# arr = [1, 2, 4]
# arr.insert(2, 3)  # Insert 3 at index 2
# print(arr)  # [1, 2, 3, 4]

# # DELETION
# arr = [1, 2, 3]
# arr.pop(1)  # Remove element at index 1
# print(arr)  # [1, 3]

# # SEARCHING
# arr = [5, 3, 8, 2]
# key = 8
# for i in range(len(arr)):
#     if arr[i] == key:
#         print(f"Found at index {i}")
#         break
# REVERSING OF AN ARRAY WITHOUT REVERSE()
# arr = [1, 2, 3, 4]
# for i in range(len(arr)//2):
#     arr[i], arr[-i-1] = arr[-i-1], arr[i]
# print(arr)

# arr = [1, 2, 3, 4]
# is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
# print("Sorted" if is_sorted else "Not Sorted")

# arr = [1, 2, 3, 4]
# # sum= 0
# key = 2
# low = 0
# high = len(arr)-1
# mid = (low + high)//2
# for i in range(len(arr)):
#     sum+=arr[i]
# print(f"the sum is present at {sum}")

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
        
#         if arr[mid] == target:
#             return mid  # Found → return index
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
    
#     return -1  # Not found

# # Example usage
# arr = [10, 20, 30, 40, 50, 60]
# target = int(input("Enter the number to search: "))

# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")

# arr= [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,19,20]
# counteven = 0
# countodd = 0
# for a in arr:
#     if a % 2 ==0:
#         counteven+=1
#         print(f"it is even and total of them is {counteven}")
#     else:
#         countodd+=1
#         print(f"it is odd and total of them is {countodd}")

# def count(arr):
#     counteven = 0
#     countodd = 0
#     for a in arr:
#         if a % 2 == 0:
#             counteven+=1
#         else:
#             countodd+=1
#     return counteven,countodd
    
# arr= [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,19,20]
# countodd, counteven = count(arr)

# def count(arr, counts):
#     # Define a function that takes the list 'arr' and a dictionary 'counts'

#     for a in arr:
#         # Loop through each element

#         if a % 2 == 0:
#             # If even,

#             counts["even"] += 1
#             # Increment the value stored at key "even"

#         else:
#             # If odd,

#             counts["odd"] += 1
#             # Increment the value stored at key "odd"


# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,19,20]
# # Define the input array

# counts = {"even": 0, "odd": 0}
# # Create a dictionary with two keys and initial counts

# count(arr, counts)



# print(f"it is even and total of them is {counts['even']}")
# print(f"it is odd and total of them is {counts['odd']}")


# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,19,20]

# counteven = 0
# countodd = 0

# for num in arr:
#     if num % 2 == 0:
#         counteven += 1
#     else:
#         countodd += 1

# print(f"It is even and total of them is {counteven}")
# print(f"It is odd and total of them is {countodd}")


# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,17,19,20]

# counteven = sum(1 for num in arr if num % 2 == 0)
# countodd = len(arr) - counteven

# print(f"It is even and total of them is {counteven}")
# print(f"It is odd and total of them is {countodd}")

# def rotate_left(arr, k):
#     n = len(arr)
#     k = k % n   # handle if k > n
#     return arr[k:] + arr[:k]

# def rotate_left(arr, k):
#     n = len(arr)
#     k = k % n
#     result = []
#     for i in range(k,n):
#         result.append(arr[i])
#     for i in range(0,k):
#         result.append(arr[i])
#     return result


# # Example usage
# arr = [1, 2, 3, 4, 5]
# k = 7
# print("Rotated array:", rotate_left(arr, k))

# def merge_sorted_arrays(arr1 , arr2):
#     i, j = 0, 0
#     merged =[]
#     while i<len(arr1) and j<len(arr2):
#         if arr1[i] < arr2[j]:
#             merged.append(arr1[i])
#             i+=1
#         else:
#             merged.append(arr2[j])
#             j+=1
#     while i<len(arr1):
#         merged.append(arr1[i])
#         i+=1
#     while j<len(arr2):
#         merged.append(arr2[j])
#         j+=1
#     return merged

# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8]
# print("Merged array:", merge_sorted_arrays(arr1, arr2))

# arr = [12, 35, 1, 10, 36, 40]

# # Step 1: assume first two elements are largest and second largest
# largest = arr[0]
# second_largest = -1   # or you can use None if you want

# # Step 2: loop through array
# for num in arr:
#     if num > largest:  
#         second_largest = largest  # update second largest
#         largest = num             # update largest
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Largest:", largest)
# print("Second largest:", second_largest)

# Example: Pair sum in sorted array
# arr = [1, 2, 3, 4, 6]
# target = 6
# left, right = 0, len(arr) - 1

# while left < right:
#     curr_sum = arr[left] + arr[right]
#     if curr_sum == target:
#         print("Pair:", arr[left], arr[right])
#         break
#     elif curr_sum < target:
#         left += 1
#     else:
#         right -= 1

# Example: Max sum of subarray of size k
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum += arr[i] - arr[i-k]   # Slide window
#     max_sum = max(max_sum, window_sum)

# print("Max sum:", max_sum)

# def min_subarray_len(target, arr):
#     n = len(arr)
#     start = 0
#     window_sum = 0
#     min_len = float("inf")   # store minimum length

    # for end in range(n):
    #     window_sum += arr[end]   # expand window

#         # shrink window while condition is met
#         while window_sum >= target:
#             min_len = min(min_len, end - start + 1)
#             window_sum -= arr[start]
#             start += 1

#     return 0 if min_len == float("inf") else min_len


# # Example
# arr = [2, 3, 1, 2, 4, 3]
# target = 7
# print("Minimum subarray length:", min_subarray_len(target, arr))


# def max_subarray_len(s):
#     start = 0    
#     sub_arr = []
#     max_len = 0
#     result = " "


#     for end in range(len(s)):
#         while s[end] in sub_arr:
#             sub_arr.remove(s[start])
#             start += 1
#         sub_arr.append(s[end])

#         if len(sub_arr) > max_len:       # update only when we get a new max
#             max_len = len(sub_arr)
#             result = "".join(sub_arr) 
#     return max_len , result

# s =  "acacbb"

# print("Maximum subarray length:", max_subarray_len(s))



# def first_negative_in_window_simple(arr, k):
#     n = len(arr)              # total number of elements
#     result = []               # will store the first negative for each window

#     # loop over all starting indices of windows of size k
#     for i in range(n - k + 1):    # windows: [i .. i+k-1]
#         first_neg = 0             # default = 0 (means “no negative found yet”)

#         # scan the current window to find the first negative
#         for j in range(i, i + k): # j walks inside the window
#             if arr[j] < 0:        # found a negative?
#                 first_neg = arr[j]  # record it
#                 break               # stop scanning this window (we only need the first)

#         result.append(first_neg)    # store answer for this window

#     return result                   # answers for all windows


# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3
# print("First negative numbers in each window:", first_negative_in_window_simple(arr, k))

# def longest_subsequence_sum_leq_target(arr, target):
#     subseq = []
#     total = 0

#     for num in arr:
#         if total + num <= target:
#             subseq.append(num)
#             total += num
#         else:
#             # if we can replace a bigger element with current smaller one
#             if subseq and max(subseq) > num:
#                 total -= max(subseq)
#                 subseq.remove(max(subseq))
#                 subseq.append(num)
#                 total += num

#     return len(subseq), subseq


# # Example
# arr = [2, 1, 5, 2, 3, 2]
# target = 7
# print("Longest subsequence length and subsequence:", longest_subsequence_sum_leq_target(arr, target))

# def count_subarrays_product_less_than_k(arr, k):
#     if k <= 1: return 0  # product can never be < k
#     prod = 1
#     start = 0
#     count = 0

#     for end in range(len(arr)):
#         prod *= arr[end]

#         while prod >= k:   # shrink if product too large
#             prod //= arr[start]
#             start += 1

#         # all subarrays ending at 'end' and starting between [start, end]
#         count += (end - start + 1)

#     return count


# # Example
# arr = [10, 5, 2, 6]
# k = 100
# print("Count of subarrays with product < k:", count_subarrays_product_less_than_k(arr, k))

















