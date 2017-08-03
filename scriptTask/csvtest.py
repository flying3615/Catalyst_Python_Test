import csv

import re


def parseFile(filePath):
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


def insertDB():
    header, values = parseFile("/Users/liuyufei/Documents/Learn/Catalyst_Python_Test/users.csv")
    sql = "INSERT INTO USER("

    # record the index of concerned column
    name_index = None
    surname_index = None
    email_index = None

    for index, column in enumerate(header):
        if 'name' == column.strip(): name_index = index
        if 'surname' == column.strip(): surname_index = index
        if 'email' == column.strip(): email_index = index
        sql += column.strip() + ","
    sql = sql[:-1] + ") VALUES ("

    for record in values:
        continue_outer = False
        insert_sql = sql
        for index, col_value in enumerate(record):
            if index == name_index or index == surname_index: col_value = col_value.strip().title()
            if index == email_index:
                # regexp check
                if not re.match(r"[^@]+@[^@]+\.[^@]+", col_value.strip()):
                    continue_outer = True
                    print col_value+" is not a valid email"
                else:
                    col_value = col_value.strip()
            insert_sql += "'" + col_value + "',"
        if continue_outer: continue
        insert_sql = insert_sql[:-1] + ")"
        print insert_sql


insertDB()
