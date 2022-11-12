#program to find three sides of a triangle and an equilateral, isosceles or scalene traingle ?
s1=int(input("Enter first side of traingle: "))
s2=int(input("Enter the second side of traingle: "))
s3=int(input("Enter the third side of traingle: "))
if s1==s2 and s2==s3:
    print("Equilateral Traingle")
if (s1==s2 and s2!=s3) or (s2==s3 and s2!=s3) \
        or (s1==s3 and s1!=s2):
    print("Isosceles Trainagle")
if s1!=s2 and s1!=s3 and s2!=s3:
    print("Scalene Traingle")
