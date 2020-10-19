def foo():
    try:
        1/0
    except FileNotFoundError as e:
        print('{} {} {}'.format(e._class, e.errno, e.strerror))

    finally:
        print('清理工作')
        return


try:
    foo()
except Exception as e:
    print('e-----')
finally:
    print('===========')