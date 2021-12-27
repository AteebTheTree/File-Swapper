file1path = input("Enter first file path: ")
file2path = input("Enter second file path: ")

file1 = open(file1path, "r")
file2 = open(file2path, "r")

file1data = file1.read()
file2data = file2.read()

file1.close()
file2.close()

file1 = open(file1path, "w")
file2 = open(file2path, "w")

file1.write(file2data)
file2.write(file1data)

file1.close()
file2.close()

print("This is done")
