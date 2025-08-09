# Read Function
file = open("sample.txt", 'r')
text = file.read()  # this will print everything
print("-: This is a Read Function :- \n")
print(text)
file.close()

# ReadLine Function
file = open("sample.txt", 'r')
line = file.readline()  # this will print the first line only
line2 = file.readline()  # this will print the second line only
print("-: This is a ReadLine Function :- \n")
print(line)
print(line2)
file.close()