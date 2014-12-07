__author__ = 'glove'

#!/usr/bin/python

import sys,traceback
import psycopg2
import argparse 
import datetime as dt

connection_string = "dbname='' user='' host='' port='' password=''"

TABLE = ''
COLUMN = 'data'

def connect():
    '''
     :param
     :return:
    '''
    try:
        conn = psycopg2.connect(connection_string)
        cursor = conn.cursor()
    except KeyboardInterrupt:
        print "Shutdown requested because couldn't connect to DB"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    return (conn,cursor) 

def parse_cmd():
  '''
  '''
  parser = argparse.ArgumentParser(description='Provide the file name and I will parse it')
  parser.add_argument('filename', type=argparse.FileType('r'),  help ='filename of the file to be chomped', nargs=1)
  args = parser.parse_args()
  for line in args.filename:  # <<<< prob not do this
      #FILE =line.readlines()
      return line

def chomp(connection, cursor,document):
    '''
    '''
    #time_now = dt.datetime.now()
    count = 0
    for line in document:
        #print line
	#sys.exit(187)
        SQL= "INSERT INTO %(table)s (%(column)s) VALUES ( \'%(data)s\' )" % {"table":TABLE, "column":COLUMN, "data":line.strip()}
        #print cursor.mogrify(SQL)
        cursor.execute(SQL)
	if count == 7500:
          connection.commit()
          print "7.5K grand later" 
          count = 0
        count = count + 1 
    connection.commit()
    connection.close()

if __name__ == "__main__":
   '''
   '''
    connection, cursor = connect()
    time_now = dt.datetime.now()
    #print parse_cmd()
    #sys.exit(187)
    chomp(connection,cursor,parse_cmd())
    time_later = dt.datetime.now()
    print "Time Delta: ", time_later - time_now
