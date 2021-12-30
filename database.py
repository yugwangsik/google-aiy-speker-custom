import pymysql


def myDB(user_say):
    db = pymysql.connect(
            host = '211.117.3.146',
            user='yu',
            passwd='1234',
            db='testDB',
            port=10002,
            charset='utf8'
    )
    cursor = db.cursor()

    print(type(user_say))
    query = "select val from testVal where list = '" + user_say + "'"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    db.close()

    return result

