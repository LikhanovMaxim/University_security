import Caesar
# import read_write_file
from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write


def main():
    source_text = read('f1.txt')
    print('source_byte=', source_text[0:15])

    # text = transform_to_text(source_text)
    text = transform_code_to_text(source_text)
    print('source_text=', text)

    encrypt_text = Caesar.encrypt_data(source_text, key=67)
    print('encrypt_byte=', encrypt_text[0:15])

    print('encrypt_text=', transform_code_to_text(encrypt_text))

    write('f1_encrypt.txt', encrypt_text)


def transform_code_to_text(source_text):
    return ''.join([chr(s) for s in source_text[0:15]])


def transform_to_text(data):
    text = ''
    for i in data[0:15]:
        text += chr(i)
    return text


def first_task():
    key = 37
    m = 24
    c = Caesar.encrypt(m, key)
    print('c=', c)
    m1 = Caesar.decrypt(c, key)
    print('m1=', m1)
    data = [34, 67, 123, 79, 201]
    encrypt_data = Caesar.encrypt_data(data, key)
    print('encrypt_data =', encrypt_data)
    decrypt_data = Caesar.decrypt_data(encrypt_data, key)
    print('decrypt_data =', decrypt_data)


if __name__ == '__main__':
    main()
