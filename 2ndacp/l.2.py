# ReadLines Function
file = open("sample.txt", 'r')
lines = file.readlines()
print(lines)
for t in lines:  # Using loop
    print(t.strip())
file.close()