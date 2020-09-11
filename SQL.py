import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='firstbd',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
    #     sql = "INSERT INTO `pandemic` (country, cases, recoveries, deaths) VALUES ('Canada','50000', '34567','3500')"
    #     cursor.execute(sql)
        pass
    
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()
        

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM pandemic"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result) 
finally:
    connection.close()