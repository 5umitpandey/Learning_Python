#Reading
f = open(r"D:\TIET\PC\MyFile.txt", "r")
print(f.read(10))
print(f.read())
f.close()

#Readline
f = open(r"D:\TIET\PC\MyFile.txt", "r")
print(f.readline())
f.close()

#Splitting
f = open(r"D:\TIET\PC\MyFile.txt", "r")
for line in f.readlines():
    print(line.split())

#Appending
f = open(r"D:\TIET\PC\MyFile.txt", "a")
f.write(" Now the file has more content")
f.close()
  
#Overwriting
f = open(r"D:\TIET\PC\MyFile.txt", "w")
f.write("All gone!")
f = open(r"D:\TIET\PC\MyFile.txt", "r")
print(f.read())
f.close()

#Creating
f = open(r"D:\TIET\PC\MyFile1.txt", "x")
f.write("New File New Text\nInsert anything here")
f = open(r"D:\TIET\PC\MyFile1.txt", "r")
print(f.read())
f.close()

#Concatenation
f1 = open(r"D:\TIET\PC\MyFile.txt", "r")
data1 = f1.read()
f2 = open(r"D:\TIET\PC\MyFile1.txt", "r")
data2 = f2.read()

f = open(r"D:\TIET\PC\MyFile_&_MyFile1.txt", "w")
f.write(data1 + "\n" + data2)
f = open(r"D:\TIET\PC\MyFile_&_MyFile1.txt", "r")
print(f.read())
f.close()

#Copying into new file
input_file = open(r"D:\TIET\PC\MyFile1.txt", "r")
output_file = open(r"D:\TIET\PC\MyFile2.txt", "w")
output_file.write(input_file.read())
output_file.close()

#Deleting
import os
os.remove(r"D:\TIET\PC\MyFile2.txt")

#Rename
import os
os.rename(r"D:\TIET\PC\MyFilee.txt", r"D:\TIET\PC\MyFileee.txt")

#Del entire directory
import os
os.rmdir("MyFolder")

#Make directory
import os
os.mkdir("MyFolder")

# tell (current position) and seek (reposition)
f = open(r"D:\TIET\PC\MyFile.txt", "r+")
str = f.read(5)
print(str)

pos = f.tell()
print("Current pos = ", pos)

pos = f.seek(10, 0)
print("Current pos = ", pos)

print(f.read(10))
f.close()


#Q
# Write a program to store numbers 1 to 19 in a FILE , 
# then count the even and odd numbers

f = open(r"D:\TIET\PC\Lab11_1.txt", "w")
for i in range(1, 20):
    f.write(f"{i}\n")

f.close()

even = 0
odd = 0

f = open(r"D:\TIET\PC\Lab11_1.txt", "r")
for i in f:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

f.close()

print("Even: ", even)
print("Odd: ", odd)



#Q
#Write a program to transfer few (let say 5) strings (separately) into a FILE

strings = ["Hello, world!", "Python is fun.", "OpenAI is amazing.", "I love programming.", "Let's code!"]

file = open(r"D:\TIET\PC\strings.txt", "w")
for string in strings:
    file.write(string + "\n")

file = open("strings.txt", "r")
content = file.read()
print(content)


#Q
# Write a program to generate random numbers between 500 to 1000.
# Then count how many are greater than 700

import random

random_numbers = [random.randint(500, 1000) for i in range(10)]
count_greater_than_700 = sum( 1 for number in random_numbers if number > 700 )

print(random_numbers)
print(count_greater_than_700)


#Q
# Write a program which should copy only those lines from a file which begin with an uppercase letter.
# (consider total five lines to execute the program and start 3 lines with uppercase in first( .txt) file.)

input_file = open(r"D:\TIET\PC\input.txt", "r")
output_file = open(r"D:\TIET\PC\output.txt", "w")

for line in input_file:
    if line[0].isupper():
        output_file.write(line)

input_file.close()
output_file.close()

f = open(r"D:\TIET\PC\output.txt", "r")
print(f.read())
f.close()




#Q
# exam.txt = "Python is a very good programming language" 
# Write a program to read and display first 15 characters. 
# Display current position of the pointer and then reposition the pointer at start and read 20 characters again.

f = open(r"D:\TIET\PC\exam.txt", "r+")
print(f.read(15))

pos = f.tell()
print("Current pos = ", pos)

pos = f.seek(0, 0)

print(f.read(20))
f.close()