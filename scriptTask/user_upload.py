#!/usr/bin/python

import getopt
import inspect
import sys
import MySQLdb
import csv
import re

from _mysql_exceptions import IntegrityError

helpInfo = """Help Info options and arguments:
--file [csv file name]  :this is the name of the CSV to be parsed
--create_table          :this will cause the MySQL users table to be built (and no further action will be taken)
--dry_run               :this will be used with the --file directive in the instance that we want to run the script but not insert into the DB. All other func ons will be executed, but the database won't be altered.
-u                      :MySQL username
-p                      :MySQL password
-h                      :MySQL host
--help                  :which will output the above list of direc ves with details.
"""

db = None
TABLE_NAME = "users"


def db_init(host, username, password, db_name):
    """init db connection"""
    global db
    frame = inspect.currentframe()
    args, _, _, values = inspect.getargvalues(frame)
    for i in args:
        if not values[i]:
            print i + " is none, please check the help info"
            sys.exit(1)
    db = MySQLdb.connect(host, username, password, db_name)


def table_setup():
    """To setup DB table by recreate"""
    print "recreate table..."
    try:
        cursor = db.cursor()
        sql_delete_table = "DROP TABLE IF EXISTS " + TABLE_NAME
        sql_create_table = "CREATE TABLE " + TABLE_NAME + """ (
                                id int(11) unsigned NOT NULL AUTO_INCREMENT,
                            name varchar(100) DEFAULT NULL,
                            surname varchar(100) DEFAULT NULL,
                            email varchar(100) DEFAULT NULL UNIQUE,
                            PRIMARY KEY (id)
                            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

        cursor.execute(sql_delete_table)
        cursor.execute(sql_create_table)
        db.commit()
    except IOError as e:
        print e
        db.rollback()


def db_close():
    """close connection if it's inited"""
    if db is not None:
        db.close()


def parse_file(filePath):
    """read csv file and extract header and records"""
    try:
        header = None
        values = []
        with open(filePath) as f:
            reader = csv.reader(f)
            for line, row in enumerate(reader):
                if line == 0:
                    header = row
                else:
                    if len(row) == 0: continue  # blank line
                    values.append(row)
        return header, values
    except IOError as e:
        print e
        sys.exit(1)


def insert_user(header, values, is_dry_run):
    """insert into DB according to the result of file content. """
    sql = "INSERT INTO " + TABLE_NAME + " ("
    # record the index of concerned column so that three columns can be any order in the file
    name_index = None
    surname_index = None
    email_index = None

    for index, column in enumerate(header):
        if 'name' == column.strip(): name_index = index
        if 'surname' == column.strip(): surname_index = index
        if 'email' == column.strip(): email_index = index
        sql += column.strip() + ","
    sql = sql[:-1] + ") VALUES ("
    try:
        for record in values:
            continue_outer = False
            insert_sql = sql
            for index, col_value in enumerate(record):
                if index == name_index or index == surname_index: col_value = col_value.strip().title()
                if index == email_index:
                    # regexp check
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", col_value.strip()):
                        continue_outer = True  # continue outer loop if email check failed
                        print col_value + " is not a valid email"
                    else:
                        col_value = col_value.strip().lower()
                insert_sql += "\"" + col_value + "\","
            if continue_outer: continue
            insert_sql = insert_sql[:-1] + ")"
            print insert_sql
            # execute sql if not dry run
            if not is_dry_run:
                cursor = db.cursor()
                try:
                    cursor.execute(insert_sql)
                    print " Done"
                except IntegrityError:
                    print "insert failed due to integrity violated for " + col_value
                    continue
            else:
                print "data not inserted due to in dry run model"
        db.commit()
    except IOError as e:
        # Rollback in case there is any error
        print e
        db.rollback()


def main():
    is_dry_run = False
    mysql_username = None
    mysql_password = None
    mysql_host = None
    reset_table = None

    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:p:h:", ["help", "file=", "create_table", "dry_run"])
        for op, value in opts:

            if op == '--help':
                print helpInfo
                sys.exit(0)

            if op == '-u':
                mysql_username = value

            if op == '-p':
                mysql_password = value

            if op == '-h':
                mysql_host = value

            if op == '--create_table':
                reset_table = True

            if op == '--file':
                file_path = value
                if "csv" not in file_path:
                    print "file " + file_path + " is not supported"
                    sys.exit(1)

            if op == '--dry_run':
                is_dry_run = True

        db_init(host=mysql_host, username=mysql_username, password=mysql_password, db_name="wordpress")
        print "after init connection..."
        if reset_table: table_setup()
        header, values = parse_file(file_path)
        insert_user(header, values, is_dry_run)
    except getopt.GetoptError as ge:
        print "Unexpected option " + ge.opt + helpInfo
        sys.exit(1)
    finally:
        db_close()


if __name__ == "__main__":
    main()
