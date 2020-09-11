import pymysql.cursors
import datetime
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='shopping',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def insert_customer(name,age,address):

    with connection.cursor() as cursor:
        # Create a new record
        sql = f"INSERT INTO customer(name,age,address) VALUES('{name}' ,{age} ,'{address}' )"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    
def insert_product (name,price,qty,weight):
    with connection.cursor() as cursor:
        # Create a new record
        sql = f"INSERT INTO product(name,price,qty,weight) VALUES('{name}' ,{price} ,{qty} ,'{weight}') "
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

def insert_purchase (cust_id,prod_id,qty,total_price,order_date):

    with connection.cursor() as cursor:
        # Create a new record
        sql = f"INSERT INTO purchase(cust_id,prod_id,qty,total_price,order_date) VALUES({cust_id} ,{prod_id},{qty},{total_price},'{order_date}') "
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    
#insert_customer("ogechi", 38 ,"12a,navy str,satelite town,lagos")
#insert_product("isi ewu",3500,1,"500g")
insert_purchase(1,1,1,3500,"2020-08-11")