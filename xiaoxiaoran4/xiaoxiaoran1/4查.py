import pymysql
def main():
    #conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='xiaoxiaoran',charset='utf8')#字典型>>>
    conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='xiaoxiaoran',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            ree = cursor.execute('select * from users')
            # for row in cursor.fetchall():   #元组
            #     print(f'id:{row[0]}')
            #     print(f'username:{row[1]}')
            #     print(f'password:{row[2]}')
            #     print('------>')

            for row in cursor.fetchall():
                print(row['id'],end='\t')
                print(row['username'],end='\t')
                print(row['password'])

            #print(cursor.fetchone())
            #print(cursor.fetchmany(3))
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close
if __name__ == '__main__':
    main()




