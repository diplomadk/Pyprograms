#write a program to add item in a tuple ?
tuplex = (4, 6, 2, 8, 3, 1)
print("Original tuple =", tuplex)
tuplex = tuplex + (9,)
print("Using + Operator ", tuplex)
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print("adiing items in a specific index ",tuplex)
listx = list(tuplex)
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print("converting the tuple to list ",tuplex)
