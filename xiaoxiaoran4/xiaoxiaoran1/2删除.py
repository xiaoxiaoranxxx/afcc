import pymysql
def main():
    xx = input('要删的..')
    try:
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='xiaoxiaoran',charset='utf8')
        with conn.cursor() as cursor:
            ree = cursor.execute('delete from users where id=%s',(xx,))
            if ree == 1:
                print()
                print('添加成功')
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close
if __name__ == '__main__':
    main()




