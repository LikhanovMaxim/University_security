from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write
import detectEnglish

COUNT = 256


def encrypt(symbol, key):
    c = (symbol + key) % COUNT
    return c


def decrypt(symbol, key):
    c = (symbol - key) % COUNT
    return c


def encrypt_data(data, key):
    cypher_data = []
    for symbol in data:
        encrypted_symbol = encrypt(symbol, key)
        cypher_data.append(encrypted_symbol)
    return cypher_data


def decrypt_data(data_c, key):
    data = []
    for symbol in data_c:
        m = decrypt(symbol, key)
        data.append(m)
    return data


def first_example():
    key = 37
    m = 24
    c = encrypt(m, key)
    print('c=', c)
    m1 = decrypt(c, key)
    print('m1=', m1)
    data = [34, 67, 123, 79, 201]
    encrypt_bytes = encrypt_data(data, key)
    print('encrypt_data =', encrypt_bytes)
    decrypt_bytes = decrypt_data(encrypt_bytes, key)
    print('decrypt_data =', decrypt_bytes)


def decrypt_file_example(encrypt_txt, decrypt_txt, key):
    encrypt_bytes = read(encrypt_txt)
    print('encrypt_data=', encrypt_bytes)

    decrypt_bytes = decrypt_data(encrypt_bytes, key)
    print('decrypt_data=', decrypt_bytes)

    print('decrypt_text=', transform_code_to_text(decrypt_bytes))

    write(decrypt_txt, decrypt_bytes)


def encrypt_file_example(file, encrypt_txt, key):
    source_text = read(file)
    print('source_byte=', source_text[0:15])

    # text = transform_to_text(source_text)
    text = transform_code_to_text(source_text)
    print('source_text=', text)

    encrypt_text = encrypt_data(source_text, key)
    print('encrypt_byte=', encrypt_text[0:15])

    print('encrypt_text=', transform_code_to_text(encrypt_text))

    write(encrypt_txt, encrypt_text)


def transform_code_to_text(source_text):
    return ''.join([chr(s) for s in source_text])


# Task 1: decrypt a file
def decrypt_text_file(encrypt_file, save_file):
    encrypt_bytes = read(encrypt_file)
    key = find_key_for_text(encrypt_bytes)
    if key != -1:
        write(save_file, decrypt_data(encrypt_bytes, key))
    else:
        print('We could not find a key :(')


def find_key_for_text(encrypt_bytes):
    key = -1
    for i in range(0, COUNT):
        decrypt_bytes = decrypt_data(encrypt_bytes[0:20], i)
        text = transform_code_to_text(decrypt_bytes)
        print('key=', i)
        print('decrypt_data=', text)
        if detectEnglish.isEnglish(text):
            print('Find! Key=', i)
            key = i
            break
    return key


def find_key_for_image(encrypt_bytes, first_byte=137, second_byte=80):
    key = -1
    for i in range(0, COUNT):
        decrypt_bytes = decrypt_data(encrypt_bytes[0:10], i)
        # print('key=', i)
        # print('decrypt_data=', decrypt_bytes)
        # print('decrypt_data=', decrypt_bytes[0])
        # print('decrypt_data=', decrypt_bytes[1])
        if decrypt_bytes[0] == first_byte and decrypt_bytes[1] == second_byte:
            print('Find! Key=', i)
            key = i
            break
    return key


def decrypt_png_file(encrypt_file, save_file):
    encrypt_bytes = read(encrypt_file)
    key = find_key_for_image(encrypt_bytes)
    if key != -1:
        write(save_file, decrypt_data(encrypt_bytes, key))
    else:
        print('We could not find a key :(')


# Task 2: decrypt a file
def decrypt_bmp_file(encrypt_file, save_file):
    encrypt_bytes = read(encrypt_file)
    key = find_key_for_image(encrypt_bytes, 66, 77)
    if key != -1:
        write(save_file, decrypt_data(encrypt_bytes, key))
    else:
        print('We could not find a key :(')


def encrypt_file_after_n_bytes(file, encrypt_txt, key=231, n=50):
    source_bytes = read(file)
    encrypt_bytes = encrypt_data(source_bytes[n:], key)
    write(encrypt_txt, source_bytes[0:n] + encrypt_bytes)
