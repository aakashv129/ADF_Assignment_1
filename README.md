# ADF_Assignment_1
1.Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.

2.Program to read a CSV (CSV with n number of columns) and store it in DICT of list.

import csv module.
choose the csv file and read the file.
csv.DictReader(file) to convert csv file into Dictionary of list.
print the Dictionary.

3.Program to Print all Prime Numbers in an Interval of 5 seconds

import time function.
Read the lower and upper bound input.
For loop that define the range(lower,upper) to print the prime numbers between the bound.
Check if the number is a positive number>1.
Next,for loop that defines the range(2,number) to iterate the numbers within the range.
If loop to check whether the number is divisible by iterator if so break the loop else print the value.
time.sleep(5) to delay the printing of the next prime number.
prime(2,10)=2 3 5 7

4.Program to Find HCF or GCD

Read the two values as input.
Checking the minimum of two values to find GCd.
For loop to iterate from 1 to the minimum number.
If the value divides both the numbers then the value is the gcd.
GCD(2,6)=2

5.Program to Convert Decimal to Binary, Octal and Hexadecimal

Read the decimal value as input.
Binary:
  Modulo the decimal value by 2.
  Append in the list.
  Divide the decimal value by 2.
Reverse the list and the value in the list is the binary value of the number.

Octal:
  Modulo the decimal value by 8.
  Append in the list.
  Divide the decimal value by 8.
Reverse the list and the value in the list is the octal value of the number.

Hexadecimal:
  Modulo the decimal value by 16.
  if the modulo value is less than 10 then append the same number in the list.
  Else if the modulo value is greater than or equal to 10 and less than 16 the append A for 10,B for 11,......,F for 15 in the list. 
  Divide the decimal value by 16.
Reverse the list and the value in the list is the binary value of the number.

6.Program to Find ASCII Value of Character

Read the character as input.
ord(character) function converts the character to respective value.

7.Program to get an application (name , age , gender, salary, state, city)

Read the input values(name,age,gender,salary,state,city)
Declare the class.
Initialize the local variables.
Declare the set function to assign given values to the values inside the class.
Declare the get function to print the input values.
Create the object for the class and call the set/get functions.
