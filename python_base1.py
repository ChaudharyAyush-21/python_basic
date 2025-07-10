#  all the basic of the python 


# choco = ["candy","burfy","icecream"]
# choco.sort(reverse= True)
# print(choco)



# choco1 = "candy"
# res = choco1[::-1]
# print(res)

# def fibo(n):
#     if n <=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# n =int(input("enter the number you like"))
# for i in range(n):
#     print(fibo(i),end=" ")


# def prime(n):
#     if n<=1:
#         return False
#     else:
#         isprime = True
#         for i in range(2,n):
#             if n % i == 0 :
#                 isprime = False
#         return isprime        
            
# n = 10
# print(f"Is {n} is prime ? {prime(n)} ")

# def prime(n):
#     if n<=1:
#         return False
#     else:
#         isprime = True
#         for i in range(2,n):
#             if n % i == 0 :
#                 isprime = False
#         return isprime        
            
# n = 10
# print(f"Is {n} is prime ? {prime(n)} ")



# def prime(num):
#     if num<=1:
#         return False
#     else:
#         isprime = True
#         for i in range(2,num):
#             if num % i == 0 :
#                 isprime = False
#         return isprime        
            
# for num in range(1, 21):
#     if prime(num):
#         print(num, end=" ")



# list1 = [1, 2, 2, 3, 4, 4, 5]    #remove duplicate
# print(set(list1))

# from collections import Counter
# list2 = [3, 1, 3, 2, 3, 2, 1, 3]
# ctr = Counter(list2)
# print(ctr.most_common(1))

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict1.update(dict2)
# # res = {**dict1, **dict2}
# # print(res)
# print(dict1)

# def subsequence(arr , index = 0 ,current = ""):
#     if index == len(arr):
#         print(current)
#         return 
#     subsequence(arr , index + 1 , current + arr[index])  #include subsequence         #for string
#     subsequence(arr , index + 1 , current)    #exclude subsequence
# arr = "abc"
# subsequence(arr)

                        #OR


# from itertools import combinations

# def generate_subsequences(s):
#     subsequences = []

#     # Generate subsequences of all lengths (1 to len(s))
#     for r in range(1, len(s) + 1):
#         for subseq in combinations(s, r):  # Generate subsequences of length `r`
#             subsequences.append("".join(subseq))  # Convert tuple to string

#     return subsequences

# # Example usage
# s = "abc"
# print("All Subsequences:", generate_subsequences(s))



# def subsequence(arr , index = 0 ,current = []):
#     if index == len(arr):
#         print(current)
#         return 
#     subsequence(arr , index + 1 , current + [arr[index]])  #include subsequence       #for list
#     subsequence(arr , index + 1 , current)    #exclude subsequence
# arr = [1,2,3]
# subsequence(arr)


from itertools import combinations
def list_seq(lst):
    sebsequence = [[]]

    for r in range(1 , len(lst)+1):
        for sub_seq in combinations(lst ,r):
            sebsequence.append(list(sub_seq))
    return sebsequence
lst = [1, 2, 3]
print("All Subsequences:", list_seq(lst))


# def subsequence(arr , index = 0 ,current =set(),elements = None):
#     if elements is None:
#         elements = list(arr)

#     if index == len(elements):
#         print(current)
#         return 
#     subsequence(arr , index + 1 , current | {elements[index]},elements)  #include subsequence         #for set
#     subsequence(arr , index + 1 , current)    #exclude subsequence
# arr = {1,2,3}
# subsequence(arr)


# from itertools import combinations
# def list_seq(lst):
#     elements = list(lst)
#     sebsequence = []

#     for r in range(1 , len(elements)+1):
#         for sub_seq in combinations(elements ,r):
#             sebsequence.append(sub_seq)
#     return sebsequence
# lst = [1, 2, 3]
# print("All Subsequences:", list_seq(lst))



# def reverse_string(s):
#     if len(s) == 0:  # Base case
#         return s
#     return s[-1] + reverse_string(s[:-1])  # Recursive call

# print(reverse_string("hello"))
# print(str)

# def is_palindrome(s):
#     if len(s) <= 1:  # Base case: Single character or empty string is always a palindrome
#         return True
#     if s[0] != s[-1]:  # If first and last characters don't match, it's not a palindrome
#         return False
#     return is_palindrome(s[1:-1])  # Recursive call with inner substring

# # Test Cases
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello")) 

# class student:

#         def __init__(self,name,rollno,marks):
#             self.name = name
#             self.rollno = rollno
#             self.marks = marks

#         def display_info(self):
#             print(f"student: {self.name} , rollno = {self.rollno}")
#             print("marks",self.marks)

#         def calculate_avg(self):
#             total_marks = sum(self.marks.values())
#             num_subjects = len(self.marks)
#             return total_marks / num_subjects if num_subjects > 0 else 0
                

#         def add_marks(self,subject,mark):
#             self.marks[subject] = mark
#             print(f"Updated Marks: {self.marks}")     


# s1 = student("Alice",101,{"Math":85, "Science":90})
# s1.display_info()
# s1.calculate_avg()
# s1.add_marks("English",50)

# class BankAccount:
#     def __init__(self, account_number, balance, pin):
#         self._account_number = account_number  # Protected attribute
#         self._balance = balance  # Protected attribute
#         self.__pin = pin  # Private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount}. New Balance: {self._balance}")
#         else:
#             print("Invalid deposit amount!")

#     def withdraw(self, amount, pin):
#         if pin == self.__pin:
#             if amount > 0 and amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrawn {amount}. Remaining Balance: {self._balance}")
#             else:
#                 print("Insufficient balance or invalid amount!")
#         else:
#             print("Invalid PIN!")

#     def get_balance(self, pin):
#         if pin == self.__pin:
#             return f"Account Balance: {self._balance}"
#         else:
#             return "Invalid PIN!"

# # Example Usage
# acc = BankAccount("12345678", 5000, 1234)
# acc.deposit(1000)
# acc.withdraw(2000, 1234)
# print(acc.get_balance(1234))  # Should show balance
# print(acc.get_balance(0000)) 

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}")

# # Child class for Cars
# class Car(Vehicle):
#     def __init__(self, brand, model, year, number_of_seats):
#         super().__init__(brand, model, year)  # Inheriting from Vehicle
#         self.number_of_seats = number_of_seats

#     def display_info(self):
#         super().display_info()
#         print(f"Number of Seats: {self.number_of_seats}")

# # Child class for Bikes
# class Bike(Vehicle):
#     def __init__(self, brand, model, year, bike_type):
#         super().__init__(brand, model, year)
#         self.bike_type = bike_type

#     def display_info(self):
#         super().display_info()
#         print(f"Bike Type: {self.bike_type}")

# # Example Usage
# car = Car("Toyota", "Camry", 2021, 5)
# bike = Bike("Yamaha", "R15", 2022, "Sports")

# car.display_info()
# print()
# bike.display_info()



# students = ["Alice", "Bob", "Charlie", "David"]
# marks = [85, 92, 78, 90]

# for name ,mark in zip(students,marks):
#     print(f"{name} scored {mark} marks")



# numbers = [7, 3, 9, 10, 15, 24, 31]
# for index, num in enumerate(numbers):
#     if num % 2 == 0:
#         print(f"First even number is {num} at index {index}")
#         break



# Q[3]
# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 90)]
# std = sorted(students, key = lambda x : x[1],reverse=True)
# print(std) 
# high_score = any(mark > 95 for _, mark in students)
# print(high_score)

# all_passed = all(mark >= 40 for _, mark in students)
# print(all_passed)



# def k_largest_sorted(numbers, k):
#     return sorted(numbers, reverse=True)[:k]  # Sort in descending order and take first k elements

# numbers = [10, 3, 5, 8, 9, 2]
# k = 3
# print(k_largest_sorted(numbers, k))

# import heapq
# numbers = [10, 3, 5, 8, 9, 2]
# heapq.heapify(numbers)
# print(numbers)

# import heapq
# def n_largest(numbers, k):
#     return heapq.nlargest(k , numbers)
# numbers = [10, 3, 5, 8, 9, 2]
# k = 3
# res = n_largest(numbers , k)
# print(res)

# import bisect
# numbers = [1, 3, 5, 7]
# pos = bisect.bisect(numbers,6)
# print(pos)
# bisect.insort(numbers,6)
# print(numbers)

# from collections import Counter
# def fun(s):
#     std = Counter(s)
#     for chars in s:
#         if std[chars] == 1:
#             return chars
#     return None
# s = "aabbcddee"
# res = fun(s)
# print(res)

# from functools import lru_cache

# @lru_cache(maxsize=None)

# def climbing_stair(n):
#     if n<=1:
#         return 1
#     return climbing_stair(n-1)+climbing_stair(n-2) 
# res = climbing_stair(5) 
# print(res)   

# import threading
# import time
# def printing():
#     for i in range(1,4):
#         print(f"Downloading file {i}.....")
#         time.sleep(3)

#     print("All files downloaded completely!")

# thread = threading.Thread(target=printing)


# thread.start()


# import threading
# import time

# def download_file(file_name):
#     print(f"Starting download: {file_name}")
#     time.sleep(3)  # Simulate download time
#     print(f"Finished downloading: {file_name}")

# # Creating multiple threads
# threads = []
# file_names = ["file1.zip", "file2.zip", "file3.zip"]

# for file in file_names:
#     thread = threading.Thread(target=download_file, args=(file,))
#     threads.append(thread)
#     thread.start()

# # Wait for all threads to finish
# for thread in threads:
#     thread.join()

# print("All downloads completed!")

# import multiprocessing
# import time

# def square(n):
#     print(f"Processing {n}...")
#     time.sleep(3)
#     print(f"the square of the {n} is {n*n}")


# if __name__ == "__main__":  
#     numbers = [1, 2, 3, 4, 5]

#     processes = []

#     for num in numbers:
#         process = multiprocessing.Process(target=square, args=(num, ))
#         processes.append(process)
#         process.start()

#     for process in processes:
#         process.join()

#     print("all process is finished successfully")
    








