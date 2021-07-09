# SQLshrimp🦐
A CLI tool created to query a mySQL Database. Based on the python-mysqlconnector
THIS SOFTWARE was designed for the solelyCONSULTATION of a SQL DATABASE and do not provides commands to perform editing/deleting/update
This anyway can be done by using a pure SQL query.


## Installation

1) Clone or Download this project in your computer:
- `git clone git@github.com:akaped/SQLshrimp.git`
- `wget https://github.com/akaped/SQLshrimp.git `

2) Be sure to install argparse and mysql-connector before running the script:

- `pip3 install mysql-connector-python-rf==2.2.2`
- `pip3 install argparse`



## USAGE

SQL Shrimps allows you to Query ANY SQL database from CLI.
If no parameters are specified it connects to Rfam DB.
If no query is specified then it executes the one it has hardcoded in the script.

`python3 SQLshrimp.py`

or


`SQLshrimp.py [-h] [-q QUERY] [-db DB] [-usr USER] [-host HOST][-port PORT]`

### Optional arguments:
*  -h, --help            show this help message and exit
*  -q QUERY, --query QUERY Processes a Query
*  -db DB, --db DB         Defines the Db to use
*  -usr USER, --user USER  Defines the User
*  -host HOST, --host HOST Defines the Host
*  -port PORT, --port PORT Defines the Port
*  -o, --output Allows to specify a .tsv file where the results of the query will be dumped.
*  -qd, --show_databases  Allows to see all databases accessible in the SQL server
*  -qt, --show_tables  Allows to list all the tables in a database (will use the db specified by user with -db)
*  -qc, --show_columns_of_table Allows to list all columns in a table  


### IDEAS FOR FUTURE IMPLEMENTATION
* Test basic Sql Injection - by specifying GET/POST request url and the field of a form.
* Specify better: -db -table -column
* --show_entries --from_column --from_table --that_contains (if not specified *) >translate this into SQL
