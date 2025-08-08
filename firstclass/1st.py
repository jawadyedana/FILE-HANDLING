# read mode
file = open("sample.txt", 'r')  # r = read, w = write, a = append
text = file.read()
print(text)
file.close()

# write mode
file = open("sample.txt", "w")
file.write("Hey this is changed with write mode.\nThankyou for using file handling")
file.close()

file = open("sample.txt", 'r')
result = file.read()
print(result)
file.close()