# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
# def string_split(s):
#     if len(s) % 2 ==0:
#         first_half = s[0:len(s)//2]
#         second_half = s[len(s) // 2:]
#     else:
#         first_half = s[:len(s)//2+1]
#         second_half = s[len(s)//2+1:]
#     return second_half+first_half
# s="bbbbbaaaaa"
# test_result = string_split(s)
# print(f'Result: {test_result}')

# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
def unique(s):
    l=[]
    for x in s:
        if x in l:
            return False
        else:
            l+=x
    return True
s="aabcde"
test_result = unique(s)
print(f'Result: {test_result}')

