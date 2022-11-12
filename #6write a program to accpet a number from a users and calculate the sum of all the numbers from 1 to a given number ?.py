#program to accpet a number from a users and calculate the sum of all the numbers from 1 to a given number ?
# s : store sum of all numbers
s = 0
n = int(input("Enter number: "))
#run loop n times
#stop: n+1
for i in range(1, n+1, 1):
    #add current number to sum
    s += i
print("Sum is: ", s)
