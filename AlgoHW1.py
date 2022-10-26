# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# def sum_to_n(n):
#     final_sum = 0
#     for x in range(n+1):
#         final_sum+=x
#     return final_sum
#
# number = int(input('Input a number: '))
# test_result = sum_to_n(number)
# print('Result: '+str(test_result))

# Find max number from 3 values.
# Example: 124, 21, 32. Result = 124.
# def max_of_three(a, b, c):
#      if a>b and a>c:
#        return a
#      elif b>a and b>c:
#        return b
#      else:
#        return c
#
# a = int(input('Input number 1: '))
# b = int(input('Input number 2: '))
# c = int(input('Input number 3: '))
# result = max_of_three(a,b,c)
# print(f'The maximum of three numbers is {result}')

# Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).def odd_even_nums(number)
def odd_even_nums(number):
    odd_nums = 0
    even_nums = 0

    while number>0:
        current_num = number % 10
        if current_num % 2:
            odd_nums += 1
        else:
            even_nums += 1
        number = number // 10

    return [odd_nums, even_nums]

test_num = 12345
test_result = odd_even_nums(test_num)
print(test_result)
# def odd_even_num(number):
#     a=str(number)
#     count_odd=0
#     count_even=0
#     for x in a:
#         if int(x)%2==0:
#             count_even+=1
#         else:
#             count_odd+=1
#     print(f'number of odd digits: {count_odd}')
#     print(f'number of even digits: {count_even}')
# a= int(input('Input number: '))
# result = odd_even_num(a)

