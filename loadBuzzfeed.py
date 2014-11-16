__author__ = 'glove'

#!/usr/bin/python

import sys,traceback
import psycopg2
import argparse 

connection_string = "dbname='json_test' user='postgres' host='127.0.0.1' port='49192' password='postgres'"

FILE = 'daily'
TABLE = 'daily'
COLUMN = 'data'

def connect():
    '''
     :param
     :return:
    '''
    try:
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()
    except KeyboardInterrupt:
        print "Shutdown requested because couldn't connect to DB"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    return cur

def parse_cmd():
  parser = argparse.ArgumentParser(description='Provide the file name and I will parse it')
  parser.add_argument('filename', type=argparse.FileType('r'),  help ='filename of the file to be chomped', nargs=1)
  args = parser.parse_args()
  for line in args.filename:
      FILE =line.readlines()
  #for f in args.filename:
  #  print f
  #  sys.exit
  return FILE

def chomp(cursor,document):
    '''
    '''
    #print document 
 #   with open(document,'rb') as datafile:
    for line in document:
        #SQL= 'INSERT INTO %(table) \(%(column)\) VALUES (\'%(data)\')' % {"table":TABLE, "column":COLUMN, "data":line}
        #SQL = 'INSERT INTO buzzinfo(data) values (\'%s\');' % line
        #print SQL
        #print line
        #cur.execute(SQL,line)
        #print cursor.mogrify(SQL)
        #  print cur.mogrify(SQL)
        #cur.execute(SQL)
        #conn.commit()
        #print cur.mogrify(SQL)
        print line
	sys.exit(187)


print "we made it"
#conn.close()

if __name__ == "__main__":
    connect()
    chomp(connect(),parse_cmd())
    

