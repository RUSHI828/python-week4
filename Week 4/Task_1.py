# Create a file and write data into it
file = open("data.txt", "w")
file.write("Hello, this is my first file.\n")
file.write("I am an AIML student.\n")
file.close()

# Read and display the file data
file = open("data.txt", "r")
print("Original File Content:")
print(file.read())
file.close()

# Append new data to the existing file
file = open("data.txt", "a")
file.write("I am learning Python file handling.\n")
file.close()

# Display the updated file content
file = open("data.txt", "r")
print("Updated File Content:")
print(file.read())
file.close()