# SQLshrimp
A CLI tool created to query a mySQL Database. Based on the python-mysqlconnector

## Installation 
Be sure to install argparse and mysql-connector before running the script:

`pip3 install mysql-connector-python-rf==2.2.2`
`pip3 install argparse`



## USAGE

`python3 SQLshrimp.py`

or


`SQLshrimp.py [-h] [-q QUERY] [-db DB] [-usr USER] [-host HOST][-port PORT]`

  SQL Shrimps allows you to Query ANY SQLDB from CLI
 If no parameters are specified it connects to Rfam DB

* optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY Processes a Query
  -db DB, --db DB         Defines the Db to use
  -usr USER, --user USER  Defines the User
  -host HOST, --host HOST Defines the Host
  -port PORT, --port PORT Defines the Port
