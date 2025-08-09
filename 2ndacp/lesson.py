# Read Function
file = open("sample.txt", 'r')
text = file.read()  # this will print everything
print("-: hello, friends and families. :- \n")
print(text)
file.close()

# ReadLine Function
file = open("sample.txt", 'r')
line = file.readline()  # this will print the first line only
line2 = file.readline()  # this will print the second line only
print("-: to be observed  :- \n")
print(line)
print(line2)
file.close()