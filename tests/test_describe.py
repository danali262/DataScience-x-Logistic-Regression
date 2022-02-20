import os


if __name__ == '__main__':
    ret_value = os.system("python3 ../describe.py test.html")
    if ret_value == -1:
        print("Test 1: OK")
    ret_value = os.system("python3 ../describe.py dataset_empty.csv")
    if ret_value == -1:
        print("Test 2: OK")
    ret_value = os.system("python3 ../describe.py")
    if ret_value == -1:
        print("Test 3: OK")