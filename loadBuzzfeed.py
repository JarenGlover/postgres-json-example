__author__ = 'glove'

#!/usr/bin/python

import sys,traceback
import psycopg2

connection_string = "dbname='json_test' user='' host='localhost' password=''"

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

def chomp():
    '''
    '''
    with open(FILE,'rb') as datafile:
      for line in datafile:
        #SQL= 'INSERT INTO %(table) \(%(column)\) VALUES (\'%(data)\')' % {"table":TABLE, "column":COLUMN, "data":line}
        SQL = 'INSERT INTO buzzinfo(data) values (\'%s\');' % line
        #print SQL
        #print line
        #cur.execute(SQL,line)
        print cur.mogrify(SQL)
        #  print cur.mogrify(SQL)
        cur.execute(SQL)
        conn.commit()
        #print cur.mogrify(SQL)
        #sys.exit(187)


print "we made it"
conn.close()

if __name__ == "__main__":
    main()


