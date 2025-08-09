# ReadLines Function
file = open("sample.txt", 'r')
lines = file.readlines()
print(lines)
for i in lines:  # Using loop
    print(i.strip())
file.close()