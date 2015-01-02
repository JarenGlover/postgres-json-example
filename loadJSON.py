__author__ = '@JarenGlover'

#!/usr/bin/env python

import sys,traceback
import psycopg2
import argparse 
import datetime as dt

connection_string = "dbname='' user='' host='' port='' password=''"

TABLE = '' 		#Name of the table that your will be inserting data into
COLUMN = 'data' 	#JSON type column name 

def connect():
    ''' Returns a postgres database connection and cursor if succesful
     Args:
  	 None
     Returns:
     	A connection to DB --> conn
	A cursor to the DB --> cursor
     Raises:
	Exception: if the connection wasn't successful *check connnection_string variable* 
    '''
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except KeyboardInterrupt:
        print "Shutdown requested because couldn't connect to DB"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    return (conn,cursor) #please note the order of the return 

def parse_cmd():
  ''' Parse the cmd line for the file you want to process
	Args:
	     	None
	Returns:
		The file that will be parsed--> filename	
  '''
  parser = argparse.ArgumentParser(description='Provide the file name and I will parse it')
  parser.add_argument('filename', type=argparse.FileType('r'),  help ='filename of the file to be chomped', nargs=1)
  args = parser.parse_args()
  for filename in args.filename:  # <<<< parse the filename from args | maybe not best way 0_o
      return filename

def chomp(connection, cursor,document):
    ''' Process the file given and loaded into DB
	Args:
		connection: A connection to a DB
		cursor: A cursor to a DB
		document: the file you want to be processed into the DB
	Returns:
		None	
    '''
    count = 0  # to help to commit to DB after every X rows been processed 
    for line in document:
        SQL= "INSERT INTO %(table)s (%(column)s) VALUES ( \'%(data)s\' )" % {"table":TABLE, "column":COLUMN, "data":line.strip()}
        cursor.execute(SQL)
	if count == 7500:
          connection.commit()
          print "Still processing 7.5K grand later ..chomp chomp..." 
          count = 0
        count = count + 1 
    connection.commit()
    connection.close()

if __name__ == "__main__":
   ''' Main function that will run the script
   '''
   connection, cursor = connect()
   print dt.datetime.now()
   time_now = dt.datetime.now()
   chomp(connection,cursor,parse_cmd())
   time_later = dt.datetime.now()
   print "Time Delta: ", time_later - time_now
