# nums = [3, 4, -1, 1]
nums = [1,2,0]
number = [num for num in range(1,len(nums)+1) if num not in nums]
# min_num = []
# sort_num = sorted(nums)

print(number)

# def max_subarray_len(s ,t):
#     start = 0  
#     s=list(s)
#     t=list(s)  
#     sub_arr = []

#     result = " "

#     if len(t) > len(s):
#         return " "
#     elif s==t:
#         return s 
#     else:
#         for end in range(len(s)):
#             while s[end] not in sub_arr:
#                 sub_arr.remove(s[start])
#                 start += 1
#             sub_arr.append(s[end])

#             result = "".join(sub_arr) 
#     return  result

# # s =  "ADOBECODEBANC"
# # s= "A"
# # t = "ABC"
# # t="AA"

# print("Maximum subarray length:", max_subarray_len(s , t))

#output
