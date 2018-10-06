from monoalphabetic.julius_caesar import Caesar

ENCRYPT_PNG = 'f2_encrypt.png'

PNG = 'f2.png'

KEY = 67
DIRECTORY = 'resources/'
FILE = DIRECTORY + 'f1.txt'
ENCRYPT_TXT = DIRECTORY + 'f1_encrypt.txt'
DECRYPT_TXT = DIRECTORY + 'f1_decrypt.txt'
ENCRYPT_FOR_TASK_1 = DIRECTORY + 't3_caesar_c_all.txt'
ENCRYPT_FOR_TASK_2 = DIRECTORY + 'c4_caesar_c_all.bmp'
ENCRYPT_FOR_TASK_3 = DIRECTORY + 'c3_subst_c_all.png'
RESULT_TXT = DIRECTORY + 'task_1_result.txt'
RESULT_TASK_2 = DIRECTORY + 'task_2_result.bmp'
RESULT_TASK_2_1 = DIRECTORY + 'task_2_1_result.bmp'
RESULT_TASK_3 = DIRECTORY + 'task_3_result.png'


def main():
    print('Start a main function:')
    # Task 1
    Caesar.decrypt_text_file(ENCRYPT_FOR_TASK_1, RESULT_TXT)
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
