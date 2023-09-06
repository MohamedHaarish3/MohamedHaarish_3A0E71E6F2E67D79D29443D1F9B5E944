"""a program that determine whether a year entered by the user is a leap year or not using ifelif-else statements"""



print("FINDING LEAP YEAR OR NOT\n")
print("************************\n")
year = int(input("Enter the year : "))
if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   print("Entered year is a leap year..")
else:
  print("Entered year is not a leap year..")


           