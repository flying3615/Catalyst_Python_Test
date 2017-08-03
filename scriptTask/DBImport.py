import getopt
import sys

helpInfo = """Help Info options and arguments:
--file [csv file name]  :this is the name of the CSV to be parsed
--create_table          :this will cause the MySQL users table to be built (and no further action will be taken)
--dry_run               :this will be used with the --file directive in the instance that we want to run the script but not insert into the DB. All other func ons will be executed, but the database won't be altered.
-u                      :MySQL username
-p                      :MySQL password
-h                      :MySQL host
--help                  :which will output the above list of direc ves with details.
"""

try:

    opts, args = getopt.getopt(sys.argv[1:], "hu:p:h", ["file=", "create_table=", "dry_run", "help"])
    mySQL_username = None
    mySQL_password = None
    mySQL_host = None
    filePath = None

    for op, value in opts:
        if op == '-u':
            mySQL_username = value
            print "mySQL username = " + mySQL_username

        if op == '-p':
            mySQL_host = value
            print "mySQL username = " + mySQL_host

        if op == '-h':
            mySQL_host = value
            print "mySQL username = " + mySQL_host

        if op == '--file':
            filePath = value
            if "csv" in filePath:
                print "filePath = " + filePath
            #     do import
            else:
                print "file "+filePath+" is not supported"

        if op == '--dry_run':
            if not filePath:
                print "Please input file first..."

        if op == '--help':
            print helpInfo

except getopt.GetoptError as ge:
    print "Unexpected option " + ge.opt + helpInfo
