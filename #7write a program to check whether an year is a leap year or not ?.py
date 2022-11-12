#write a program to check whether an year is a leap year or not ?
year=int(input("Enter The Year: "))
if year%100==0:
    if year%400==0:
        print("Entered year is leap year")
    else:
        print("Entered year is not leap year")
else:
    if year%4==0:
        print("Entered year is leap year")
    else:
        print("Entered year is not a leap year")
