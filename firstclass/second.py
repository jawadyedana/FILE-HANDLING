# append mode 
file = open("sample.txt", "a")
file.write("\nhello this is changed with the append mode,\nthank you.")
file.close()

file = open("sample.txt", "r")
text = file.read()
print(text)
file.close()

# open the file in read mode 
file_read = open("sample.txt", "r")
print("file in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in append mode
file_append = open("sample.txt ," "a")
# append in the file 
file_append.write("\n file in append mode ***\n")
file.close()
