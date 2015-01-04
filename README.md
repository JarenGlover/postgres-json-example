My learnings with JSON + Postgres 9.3
=========
This project will hold the lessons learned from a recent data project. This project's goal was to take a MongoDB data dump and do some analysis on it. This resulted in me leveraging Postgres's JSON data type and its SQL extension to load and query the data set (~5 Million rows). 

You might be asking why Postgres? When Postgres 9.4 comes out it will be more clear. Below is a snippet from  a great [InfoQ] article. 
>PostgreSQL 9.4 Beta comes with the much-anticipated "binary JSON" type, JSONB. This new storage format for document data is higher-performance and comes with indexing, functions and operators for manipulating JSON data.

>The JSONB type is a confluence of two projects - HStore and JSON. JSONB has everything JSON had, but is more efficient in storage due to the binary representation, and faster due to indexing. Eventually, all current HStore and JSON users are expected to move to JSONB.

>Why would NoSQL features be important for PostgreSQL, when it's traditional user base has been developers needing solid relational capabilities or users switching from enterprise databases such as Oracle? Josh Berkus, one of the core team members, shares some insights.

Now back to the basics ...

Concepts covered:

1. Load the data dump into Postgres database
2. **_PENDING_ -** Lessons learned when dealing with a big data set
3. **_PENDING_ -** How to query a JSON data structure
4. **TBA**

**_Create a table with JSON data type_**
>Below is an example of how to create a table that can hold JSON structure data.
```
CREATE TABLE json_test(ID SERIAL, data JSON);
````

When you search on the internet on "how to load data into Postgres" most websites will point you to [copy] [command]. However, I found this not to work well with a dump of web related JSON data. It appears to work best when you have non-complex data that is in some delimiter separated file [ id | tree | frog | magic]. It couldn't process/parse the ton of backslashes and forward slashes which was found in my data dump of web related content (URLs, URIs, etc). 
Interestingly enough, the [Postgres Wiki] has something "unique" to say about the [copy] command.
>"COPY is not terribly smart or clever, in fact it is dumb and simple."

Sadly it took me two full days of troubleshooting the [copy] to understand it wasn't going to be my star player. I unsuccessfully tried to use some fancy sed commands to "clean" the data source. So this is why I created a nifty script to solve this problem. Honestly, not sure why this isn't something better documented on the interweb. 

****kanye shrugz****

Please note that the JSON data structure(s) have to abide by the JSON standard format. You can take a sample of your data and test it at [JSONLint] or by the below query. Fortunately, Postgres validates JSON before saving the document into the database. 
```
SELECT '{"bar": "baz", "balance": 7.77, "active":false}'::json;
                      json                       
-------------------------------------------------
 {"bar": "baz", "balance": 7.77, "active":false}
(1 row)
```
As you can see the syntax roughly follows:
```
SELECT '<JSON structure here>'::json;
```
If the command is successful you can have reasonable confidence that Postgres will processed and save the data set into the JSON data type column.

So now that you have confirmed your data is structured properly, how do you load the data into the database table? I've created a python script called [loadJSON.py] that will process a flat file that has one JSON structure per new line and insert it into the table. Please note that you will have to set the TABLE, COLUMN, and connection_string variables to match your environment.

There are three core functions that hold the core logic. 

1. connect - Create and return the connection and cursor to the database
2. parse_cmd - Parsed the cmd line using [argparse] to obtain the filename of the file that will be loaded
3. chomp - Processed line by line the filename returned by the parse_cmd function and inserts the lines into the DB and committing only after 7.5K rows have been processed. 


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
[InfoQ]:http://www.infoq.com/news/2014/05/postgresql-9-4
[argparse]:https://docs.python.org/3/library/argparse.html

