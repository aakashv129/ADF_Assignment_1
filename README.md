# ADF_Assignment_1
Read the input file from the command line argument.
Open the file in read mode if the file doesn't exit then print File not found.
Then split the words in the file into a list.

a)Print the number of words having prefix with “To” in the input file.
Declare a variable to count the prefix word "To".
For loop to access the list and check whether the word begins with "To" or not.
If the word is present the increment the variable count by 1.
Print the number of words begin with "To".

b)Print the number of words ending with “ing” in the input file.
Declare a variable to count the suffix words "ing".
For loop to access the list and check whether the word ends with "ing" or not.
If the word is ends with suffix then increment the variable count by 1.
Print the number of words ends with "ing".

c)Print the word that was repeated maximum number of times.
Declare the variable max_count to find the maximum number of times a word is repeated.
Declaring a temporary variable to store the maximaum repeating word.
For loop to iterate through the list.
Then another variable to count the number of times a single word is repeated.
Next,for loop to compare other words in the list.
If the word in list matches with other words in the list then increment count by 1.
Then finding the maximum number of times a word is repeated by comapring max_count and count.
Then storing the maximum repeated word in temporary variable and print the word.

d)Print the palindrome present in the file.
Declaring function to find the word is palindrome or not.
For loop to iterate through the list and finding whether the word is palindrome or not.
Then print the palindromic words.

e)Convert all words into unique list and print in command line.
Declare an empty list to add unique words.
For loop to iterate through the list.
Converting each words into lower() case to avoid duplicates.
Comapring words in the list with words in the result list if not present then the word is appended into the list.
Then printing the list with unique words.

f)Create a Word dict with Key as counter index and value as the words present in file and print them on screen.
Declare an empty dictionary.
Enumerate() function to generate counter index for each words in the list.
Then updating into the dictionary.
Printing the dictionary after conversion.

g)Write new file with following actions
i.Split the words based on the vowels
imported re package
re.split() function is used to split the words based on the vowels.
And then ''(empty words) are removed using while loop after splittiing.

ii.Capitalize 3rd letter of every word
String slicing is used to capitalize the 3rd letter of every word if the length of the word is less than 2 then the loop is skipped.

iii.Capitalize all characters of every 5th word in the file.
Declare the count variable.
Counting the iteration of the for loop using count variable.
If the count variable reaches 5,10,15 th wors then it is capitalized using upper() keyword.

iv.Use – in place of blank space
while writing into the file space is replaced is '-' symbol.

v.Use ; (semi-colon) for new line.
while writing into the file when new line is inserted it is replaced is ';' symbol.










