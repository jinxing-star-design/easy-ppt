tag = True
count = 0
while count < 3:
    inp_name = input("please input your username")
    inp_pwd = input("please input your password")

    if inp_name == 'jinxing' and inp_pwd == '123':
        print("successfully")
        while tag:
            cmd = input('input :')
            if cmd == 'q':
                tag = False
            else:
                print('命令{x}正在运行'.format(x=cmd))
        break
    else:
        print('账号或密码错误')
        count += 1
else:
    print("输错三次 请重新输入")