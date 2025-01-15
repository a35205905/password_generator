import random, string

def main():
    is_auto = get_is_auto()
    # is_auto = 'n'
    if is_auto == 'y':
        password_len = 16
        password_num = 5
    else:
        password_len = get_password_len()
        password_num = get_password_num()

    print('-'*20)
    for i in range(password_num):
        punctuation = '!#$%&*+-:;<>?@^_|~'
        password = ''.join(random.sample(string.digits + string.ascii_letters + punctuation, password_len))
        print(password)

    print('-'*20)

def get_is_auto():
    while True:
        is_auto = input('是否隨機生成亂數密碼？[y/n]：').lower()
        if is_auto == 'y' or is_auto == 'n':
            return is_auto

        print('輸入格式錯誤，請重新輸入！')

def get_password_len():
    while True:
        password_len = input('請選擇亂數長度[1-64]：')
        if password_len.isdigit() and int(password_len) > 0 and int(password_len) <= 64:
            return int(password_len)
                
        print('輸入格式錯誤，請重新輸入！')

def get_password_num():
    while True:
        password_num = input('請選擇亂數數量[1-20]：')
        if password_num.isdigit() and int(password_num) > 0 and int(password_num) <= 20:
            return int(password_num)
                
        print('輸入格式錯誤，請重新輸入！')


if __name__ == '__main__':
    main()