from userper import Userper

if __name__ == '__main__':
    u = Userper('login.stufinite.faith:8080')
    print(u.get_user())
    print(u.get_user(''))
