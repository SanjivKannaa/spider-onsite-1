import datetime
import mysql.connector as sql


connection = sql.connect(host='sql6.freemysqlhosting.net', user='sql6513340', password='Iluqh1ZCX3', database='sql6513340')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS login_info(
    email CHAR(9) PRIMARYKEY,
    name CHAR(10),
    password VARCHAR(256)
)''')
connection.commit()


def put_login_info(email, name, password):
    c.execute('INSERT INTO login_info(email, name, password) VALUES({}, {}, {})'.format(email, name, password))
    connection.commit()


def get_login_info(email):
    c.execute('SELECT * FROM login_info WHERE email={}'.format(email))
    return list(c.fetchall())


def signup(email, name, password1, password2):
    login_content = get_login_info(email)
    if login_content == "" and password1 == password2:
        put_login_info(email, name, password1)


def check_login(email, password):
    data = get_login_info(email)
    if email in data and password in data :
        return [True, ""]
    if data == '':
        return [False, "no user"]
    else:
        return [False, "wrong password"]