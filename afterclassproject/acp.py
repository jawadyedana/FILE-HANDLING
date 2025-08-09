# Read the file
file = open('sample.txt', 'r')
print(file.read())
file.close()

# Write to the file
file = open('sample.txt', 'w')
file.write("New content is being written.")
file.close()

# Append to the file
file = open('sample.txt', 'a')
file.write("\nThis content is being appended.")
file.close()

# Read the file again
file = open('sample.txt', 'r')
print(file.read())
file.close()