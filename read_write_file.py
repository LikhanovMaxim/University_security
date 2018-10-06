from struct import *


def read_data(file_name, buffer_size, frm):
    infile = open(file_name, 'rb')
    buffer = infile.read(buffer_size)
    data = []
    while len(buffer):
        value = unpack(frm, buffer)
        data.append(value[0])
        buffer = infile.read(buffer_size)
    infile.close()
    return data


def read_data_1byte(file_name):
    buffer_size = 1
    frm = "B"  # unsigned char
    return read_data(file_name, buffer_size, frm)


def read_data_2byte(file_name):
    buffer_size = 2
    frm = "H"  # one integer
    return read_data(file_name, buffer_size, frm)


def write_data_1byte(file_name, data):
    outfile = open(file_name, 'wb')
    frm = "B"
    i = 0
    while i < len(data):
        data1 = pack(frm, int(data[i]))
        outfile.write(data1)
        i += 1
    outfile.close()


def write_data_2byte(file_name, data):
    outfile = open(file_name, 'wb')
    frm = "H"
    i = 0
    while i < len(data):
        data1 = pack(frm, int(data[i]))
        outfile.write(data1)
        i += 1
    outfile.close()


def write_numbers(file_name, numbers):
    fo = open(file_name, 'w')
    for i in numbers:
        fo.write(str(i) + ' ')
    fo.close()


def read_numbers(file_name):
    cypher_data = read_data_1byte(file_name)
    # form string
    s = ''
    for i in cypher_data:
        s += (str(chr(i)))
    s = s.split()

    # form list of large numbers
    encrypt_nums = []
    for i in s:
        encrypt_nums.append(int(i))
    return encrypt_nums


def main():
    file_name = 'data_c.txt'
    data = read_data_1byte(file_name)
    file_name1 = 'data_2.png'
    write_data_1byte(file_name1, data)


if __name__ == '__main__':
    main()
