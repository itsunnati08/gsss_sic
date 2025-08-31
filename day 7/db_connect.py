import pymysql

connection = pymysql.Connect(
    host='localhost',
    user='root',
    password='123456789',
    database='sic',
    port=3306,
    charset='utf8mb4',
)
if connection:
    print("Connection to the database was successful.")
else: 
    print("Failed to connect to the database.")
    