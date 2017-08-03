#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("127.0.0.1", "wordpress", "wordpress", "wordpress")

# prepare a cursor object using cursor() method
cursor = db.cursor()



# Prepare SQL query to INSERT a record into the database.
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#       ('Mac', 'Mohan', 20, 'M', 2000)


sql_delete_table = "DROP TABLE catalyst_user"

sql_create_table = """CREATE TABLE catalyst_user (
                    id int(11) unsigned NOT NULL AUTO_INCREMENT,
                    name varchar(100) DEFAULT NULL,
                    surname varchar(100) DEFAULT NULL,
                    email varchar(100) DEFAULT NULL UNIQUE,
                    PRIMARY KEY (id)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
try:
    # Execute the SQL command
    cursor.execute(sql_delete_table)
    cursor.execute(sql_create_table)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
