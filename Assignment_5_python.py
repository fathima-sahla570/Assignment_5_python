# Exercise 1:Write a Python program to read a file and display its contents
with open("file_1.txt","r") as file1:
 data=file1.read()
 print(data) #O/P is "Hello Good Morning"
# # 2 Write a Python program to copy the contents of one file to another file
# # Simple file copy program
with open("file_1.txt", 'r') as file2, open('destination.txt', 'w') as dest:
    dest.write(file2.read())
print("File copied successfully!")
# # Exercise 3 Write a Python program to read the content of a file and count the total number of words in that file.
# # Count words in a file
with open('file_1.txt', 'r') as file:
 words=file.read().split()
 print("Total words:", len(words))
#  # 4:Write a Python program that prompts the user to input a string and converts it to an integer Use try-except blocks to handle any exceptions that might occur
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("Converted integer:", number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# # 5 Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.
try:
    numbers = input("Enter a list of integers (space-separated): ").split()
    for num in numbers:
        if int(num) < 0:
            print("Error: Negative numbers are not allowed!")
            break
    else:
        print("Valid list:", [int(num) for num in numbers])
except ValueError:
    print("Error: Please enter only integers!")
# # 6 Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any
# # exceptions that might occur.use the finally clause to print a message indicating that the program has finished running.
try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    average = sum(numbers) / len(numbers)
    print("Average:", average)
except ValueError:
    print("Invalid input! Please enter only integers separated by spaces.")
except ZeroDivisionError:
    print("Cannot compute average of an empty list.")
finally:
    print("Program has finished running.")

# # 7Write a Python program that prompts the user to input a filename and writes a string to that file.
# # Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
try:
    filename = input("Enter the filename: ")
    with open(filename, "w") as file:
        file.write("Hello, this is a sample text written to the file.")
    print("File has been written successfully. Welcome!")
except IOError:
    print("An error occurred while accessing the file. Please check the filename and try again.")


