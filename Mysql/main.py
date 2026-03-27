import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(host=host, user=user, port=3306, password=password, db=db_name, cursorclass = pymysql.cursors.DictCursor)
    print("successfully connected to database")

    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            print(cursor.fetchall())
            print(f"Server version: {cursor.rowcount}")
    finally:
        if connection:
            connection.close()

except Exception as ex:
    print("Connection error")
    print(ex)