__author__ = 'glove'

#!/usr/bin/python

import sys,traceback
import psycopg2

connection_string = ""

#FILE = 'sample.json'
FILE = 'buzzfeed_buzzinfo_2013_01.json'
TABLE = 'buzzinfo'
COLUMN = 'data'

#conn= psycopg2.connect(connection_string)

conn = psycopg2.connect("dbname='buzzfeed' user='glove' host='localhost' password='jaren'")
#conn = psycopg2.connect("dbname='buzzfeed' user='bz' host='localhost' password='/W9CjePoad9ZqSlp3T9lNVVV026mO1digSD0+SXJcr8='")
cur = conn.cursor()

with open(FILE,'rb') as datafile:
  for line in datafile:
    #SQL= 'INSERT INTO %(table) \(%(column)\) VALUES (\'%(data)\')' % {"table":TABLE, "column":COLUMN, "data":line}
    SQL = 'INSERT INTO buzzinfo(data) values (\'%s\');' % line
    #print SQL
    #print line
    #cur.execute(SQL,line)
    print cur.mogrify(SQL)
   # print cur.mogrify(SQL)
    cur.execute(SQL)
    conn.commit()
    #print cur.mogrify(SQL)
    #sys.exit(187)

print "we made it"
conn.close()
#if __name__ == "__main__":
#    main()


