import random, string

def main():
    is_auto = get_is_auto()
    # is_auto = 'n'
    paaword_num = 5
    if is_auto == 'n':
        password_len = 16
    else:
        password_len = get_password_len()

    print('-'*20)
    for i in range(paaword_num):
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
        password_len = input('請選擇亂數長度[1-16]：')
        if password_len.isdigit():
            password_len = int(password_len)
            if password_len > 0 and password_len <= 16:
                return password_len
                
        print('輸入格式錯誤，請重新輸入！')


if __name__ == '__main__':
    main()