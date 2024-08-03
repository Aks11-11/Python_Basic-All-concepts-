#Line-line
with open("myfile.txt") as file:
    for line in file:
        print(line)

#with_line-number
file = open('myfile.txt', 'r')
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))

#write-string
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))

#read_a-string
with open('myfile1.txt', "r+") as file:
    contents = file.read()
print(contents)

#write-an-object
contents = {"aa": 12, "bb": 21}
with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents))

#read-an-object
with open('myfile2.txt', "r+") as file:
    contents = json.load(file)
print(contents)

#delete-a-file
import os
os.remove("myfile.txt")

#check-a-date
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

#delete-a-folder
import os
os.rmdir("myfolder")
