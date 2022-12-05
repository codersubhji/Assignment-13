"""10. Write a Python script to create a list, where each element of the list is a digit of a
given number."""
li=int(input("Enter any number to create a list :"))
print([int(num) for num in str(li)])
