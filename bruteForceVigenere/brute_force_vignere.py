import csv

def encode_vigenere(message, key):
        encode_msg = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        message = message.lower()
        key_index = 0
        for index in range(0, len(message)):
            if key_index >= len(key):
                key_index = 0
            if not key[key_index].isalpha():
                key_index += 1
            if not message[index].isalpha():
                encode_msg += message[index]
                continue
            index = (alphabet.find(message[index]) - alphabet.find(key[key_index])) % len(alphabet)
            encode_msg += alphabet[index]
            key_index += 1
        return encode_msg

def decode_vigenere(message, key):
        decode_msg = ""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        key_index = 0
        message = message.lower()
        for index in range(0, len(message)):
            if key_index >= len(key):
                key_index = 0
            if not key[key_index].isalpha():
                key_index += 1
            if not message[index].isalpha():
                decode_msg += message[index]
                continue
            index = (alphabet.find(message[index]) + alphabet.find(key[key_index])) % len(alphabet)
            decode_msg += alphabet[index]
            key_index += 1
        return decode_msg

def reset_key(size, key):
    index = 0
    while index < size:
        key.append(chr(97))
        index += 1
    return key

def after(index, key):
    for i in range(index, len(key)):
        if key[i] != 'z':
            return False
    return True

def test(key):
    index = 0
    while index < len(key):
        if key[index] == 'z' and index > 0:
            if after(index, key):
                key[index - 1] = chr(ord(key[index - 1]) + 1)
        if ord(key[index - 1]) > 122:
            key[index - 1] = 'a'
        index += 1
    if key[index - 1] == 'z':
        key[index - 1] ='a'
    return key

def create_csv():
    header = ["original","offset", "message"]
    with open("decoded_message.csv", "w") as data:
        writer = csv.writer(data)
        writer.writerow(header)

def appendline(key, message, original):
    temp = [original, key, message]
    with open("decoded_message.csv", "a") as data:
        writer = csv.writer(data)
        writer.writerow(temp)

def generate_key(size, key, message):
    index = 97
    print(size)
    if size == 1:
        while index < 123:
            key[0] = chr(index)
            possibility = decode_vigenere(message,key)
            str_key = ''.join(key)
            appendline(str_key, possibility, message)
            index += 1
    else:
        last_index = len(key) - 1
        index = last_index
        i = 0
        unicode = 97
        max_possibility = 26 ** len(key)
        while i < max_possibility:
            key[index] = chr(unicode)
            possibility = decode_vigenere(message, key)
            str_key= ''.join(key)
            appendline(str_key, possibility, message)
            if unicode == 122:
                unicode = 96
                key = test(key)
            unicode += 1
            i += 1

def build_key(size, message):
    key = []
    key = reset_key(size, key)
    generate_key(size, key, message)

def brut_force_vigenere(message):
    create_csv()
    for i in range(1, len(message) + 1):
        build_key(i, message)

encoded_message = encode_vigenere("he", "test")
print("encoded message : {}".format(encoded_message))
brut_force_vigenere(encoded_message)