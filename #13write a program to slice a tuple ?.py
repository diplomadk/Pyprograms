#program to slice a tuple ?
#create a tuple
tuplex=(1, 2, 3, 4, 5, 6, 7, 8, 6, 3,)
print("Original tuple", tuplex)
_slice=tuplex[3:5]
print("Tuple [3:5]", _slice)
_slice=tuplex[:6]
print("Tuple [:6]", _slice)
_slice=tuplex[5:]
print("Tuple [5:]", _slice)
_slice=tuplex[:]
print("Tuple [:]", _slice)
_slice=tuplex[-8:-4]
print("Tuple [-8:-4]", _slice)
