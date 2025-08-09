# open file and read its content
file = open("sample.txt", "r")
print(file.read())
file.close()

# open file and read its beginning 8 characters 
file = open("sample.txt", "r")
print("\n read in parts \n")
print(file.read(8))
file.close()

# apppend your name and age to the file 
file = open("sample.txt", "a")
file.write(" hi! i am Jawad and i am 17 years old")
file.close()