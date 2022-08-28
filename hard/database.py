import mysql.connector as sql

print('making connection to db')
connection = sql.connect(host='sql6.freemysqlhosting.net', user='sql6513340', password='Iluqh1ZCX3', database='sql6513340')
c = connection.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS login_info(
    username VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100)
)''')
connection.commit()


print('made connection to db')
def init():
    c.execute('DROP TABLE login_info')
    c.execute('''CREATE TABLE IF NOT EXISTS login_info(
        username VARCHAR(100) PRIMARY KEY,
        password VARCHAR(100)
    )''')
    c.execute('INSERT INTO login_info (username, password) VALUES ("sanjiv", "sanjiv")')
    connection.commit()


def put_login_info(username, password):
    c.execute('INSERT INTO login_info (username, password) VALUES ("{}", "{}")'.format(username, password))
    connection.commit()


def get_login_info(username):
    # preventing SQLi by validating username
    username_validated = username.split()[0]
    c.execute('SELECT * FROM login_info WHERE username="{}"'.format(username_validated))
    return list(c.fetchall())


def signup(username, password1, password2):
    login_content = get_login_info(username)
    if login_content == [] and password1 == password2:
        put_login_info(username, password1)

def check_user(username):
    username_validated = username.split()[0]
    c.execute('SELECT * FROM login_info WHERE username="{}"'.format(username_validated))


def check_login(username, password):
    data = get_login_info(username)
    try:
        if username == data[0][0] and password == data[0][1] :
            return [True, ""]
        else:
            return [False, "wrong password"]
    except:
        return [False, "no user"]

print('passed database')