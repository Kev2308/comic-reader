import pymysql

connection = pymysql.connect(
    host= 'database-1.cm8y7z0ycta2.ap-northeast-1.rds.amazonaws.com',
    port= 3306,
    user= 'admin',
    password= 'Chief#143',
    db= 'database-1'
)


with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()