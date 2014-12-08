My learnings with JSON + Postgres 9.3
=========
This project will hold the lessons learned from a recent data project. This project goal was to take a MongoDB data dump and do some analysis on it. This resulted in me leveraging Postgres's JSON data type and its SQL extension to load and query the data set (~5 Million rows). 

Concepts convered:
1. Load the data dump into Postgres database
2. **_PENDING_ -** Lessons learned when dealing with a big data set on local enviroment 
3. **_PENDING_ -** How to query a JSON data struture 
4. **TBA**

**_Creating a table with JSON datatype_**
>Below is an example of how to create a table that can hold JSON struture data. 
```
CREATE TABLE json_test(ID SERIAL, data JSON);
````

When you search on the internet on how to load data into Postgres most websites will point you to [copy] [command]. However, I found this not to work well with a dump of web related JSON data. It appears to work best when you have non-complex data that is in some delimiter file. [ id | tree | frog | magic] It couldn't processed/parse the tons of backslashes and froward slashes which was found in my data dump given it held web related content (URLs, URIs, etc). 
Interesting enought the [Postgres Wiki] has something interesting to say about the [copy] command. 
>"COPY is not terribly smart or clever, in fact it is dumb and simple."

Sadly it took me two full days of troubleshooting the [copy] command by using some fancy sed commands to "clean" the data source. So this is why I created a nifty script to solve this problem and to remind myself to not to make the mistake again. Honestly, not sure why this wasn't something was documented more on the interweb. ** < kanye shrugz > ** 

Please note that the JSON data stututre(s) have to abide by the JSON standard format. You can take a sample of your data and test it at [JSONLint] or by the below query.
```
SELECT '{"bar": "baz", "balance": 7.77, "active":false}'::json;
                      json                       
-------------------------------------------------
 {"bar": "baz", "balance": 7.77, "active":false}
(1 row)
```
As you can see the systax roughly follows:
```
SELECT '<JSON struture here>'::json; 
```
If the command is succesfuly you can have reasonable confidence that Postgres will processed and save the dataset into the JSON datatype column. 

So now that you have confirmed your data struture properly, how do you load the data into the database table? I've created a python script called [loadJSON.py] that will processed a flatfile that has one JSON struture per newline and insert it into the table. Please note you will have to set the TABLE, COLUMN, and connection_string varibles to match your environment. 

There are three core functions that was hold the core logic. 
1. connect - Create and return the connection and cursor to the datbase 
2. parse_cmd - Prased the cmd line using argparse to obtain filename to be loaded into the DB
3. chomp - processed line by line the filename returned by the parse_cmd function and inserts the lines into the DB and commiting only aftering 7.5K rows has been procesesed. 


Version
----
0.1

Tech
-----------
* [Postgres] - The Database
* [Python] - Programming Language 

Required Non-Standard Modules
---
```
import [psycopg2]
```

Contact
----
Scream @ me --> [Jaren Glover]

License
----

MIT
**Free Software, Trap or Die**

[Python]:https://www.python.org/download/releases/2.7.6/
[Postgres]:http://www.postgresql.org/docs/9.3/static/release-9-3-5.html
[Jaren Glover]: https://www.twitter.com/jarenglover
[psycopg2]:http://initd.org/psycopg/
[copy]:http://www.postgresql.org/docs/9.3/static/sql-copy.html
[command]:http://stackoverflow.com/questions/20039856/import-excel-data-into-postgresql-9-3
[JSONLint]:http://jsonlint.com
[loadJSON.py]:https://github.com/GloveDotCom/postgres-json-example/blob/master/loadJSON.py
[Postgres Wiki]:https://wiki.postgresql.org/wiki/COPY

