print('Test_02.py Print')


def get_len(argv1):
    print(f'length of inputed string is {len(argv1)}.')

import sys
if __name__ == '__main__':
    argv1 = str(sys.argv[1])
    get_len(argv1)

# import sys
# if __name__ == '__main__':
#     if sys.argv[1] == 'get_len':
#         get_len(sys.argv[2])



    # ['D:\\Git\\PythonMultiprocessPractice\\Part02\\test_02.py', 'Test_01.py Print\r\n']