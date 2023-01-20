#Check wether the user-input is palindrome.

user_input = input()
all_small = user_input.lower()
orignal_seq = all_small.replace(" ",'')
reversed_seq = orignal_seq[::-1]

if orignal_seq == reversed_seq:
   print(f"{user_input} is a palindrome.")
else:
   print(f"{user_input} is not a palindrome.")
