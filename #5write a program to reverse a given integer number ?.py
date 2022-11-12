#program to reverse a given integer number ?
num = int(input('Enter The number: '))
reverse_number = 0
print("Given number ", num)
while num > 0:
     reminder = num % 10
     reverse_number = (reverse_number * 10) + reminder
     num = num // 10
print("Reverse number ", reverse_number)
