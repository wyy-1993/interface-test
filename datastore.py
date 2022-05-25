import pymysql

db = pymysql.connect(
    host = 'rm-2evdvo1hp674z596f.mysql.rds.aliyuncs.com',
    port = 3306,
    user = 'carso_noprod',
    password = '4wQ^79lr5EUvxuB2WSf',
    charset = 'utf-8',
    db = 'carso_new_dev',
)

cursor = db.cursor()

SQL = 'select * from base_user limit 1 '

cursor.close()
db.close()



