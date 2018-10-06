import Caesar
import detectEnglish
from read_write_file import read_data_1byte as read
from read_write_file import write_data_1byte as write

ENCRYPT_PNG = 'f2_encrypt.png'

PNG = 'f2.png'

KEY = 67
FILE = 'f1.txt'
ENCRYPT_TXT = 'f1_encrypt.txt'
DECRYPT_TXT = 'f1_decrypt.txt'
ENCRYPT_FOR_TASK_1 = 't3_caesar_c_all.txt'
ENCRYPT_FOR_TASK_2 = 'c4_caesar_c_all.bmp'
RESULT_TXT = 'task_1_result.txt'
RESULT_TXT_TASK_2 = 'task_2_result.bmp'


def main():
    # Task 1
    # Caesar.decrypt_text_file(ENCRYPT_FOR_TASK_1, 'task_1_result.txt')
    # Task 2
    Caesar.decrypt_bmp_file(ENCRYPT_FOR_TASK_2, RESULT_TXT_TASK_2)


def decrypt_file_example():
    Caesar.decrypt_file_example(ENCRYPT_TXT, DECRYPT_TXT, KEY)


def encrypt_file_example():
    Caesar.encrypt_file_example(FILE, ENCRYPT_TXT, KEY)


if __name__ == '__main__':
    main()
