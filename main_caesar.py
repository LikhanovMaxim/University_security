import Caesar
import substitution
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
ENCRYPT_FOR_TASK_3 = 'c3_subst_c_all.png'
RESULT_TXT = 'task_1_result.txt'
RESULT_TASK_2 = 'task_2_result.bmp'
RESULT_TASK_2_1 = 'task_2_1_result.bmp'
RESULT_TASK_3 = 'task_3_result.png'


def main():
    print('Start a main function:')
    # Task 1
    # Caesar.decrypt_text_file(ENCRYPT_FOR_TASK_1, 'task_1_result.txt')
    # Task 2
    # Caesar.decrypt_bmp_file(ENCRYPT_FOR_TASK_2, RESULT_TASK_2)
    # Caesar.encrypt_file_after_n_bytes(RESULT_TASK_2, RESULT_TASK_2_1)
    # Task 3
    # substitution.decrypt(ENCRYPT_FOR_TASK_3, RESULT_TASK_3)


def decrypt_file_example():
    Caesar.decrypt_file_example(ENCRYPT_TXT, DECRYPT_TXT, KEY)


def encrypt_file_example():
    Caesar.encrypt_file_example(FILE, ENCRYPT_TXT, KEY)


if __name__ == '__main__':
    main()
