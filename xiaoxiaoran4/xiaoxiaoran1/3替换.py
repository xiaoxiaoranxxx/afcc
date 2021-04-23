import pymysql
def main():
    username = input('要换的..:')
    id = input('id...:')
    try:
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='xiaoxiaoran',charset='utf8')
        with conn.cursor() as cursor:
            ree = cursor.execute('update users set username=%s where id=%s',(username,id))
            if ree == 1:
                print()
                print('替换成功')
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close
if __name__ == '__main__':
    main()




