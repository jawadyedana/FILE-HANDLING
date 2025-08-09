# read the first line of the file 
file = open("sample.txt", "r")
print("read first line...")
print(file.readline())
file.close()

# reaad the first three lines of the file 
file = open("sample.txt", "r")
print("read first three lines....")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

print("lines")