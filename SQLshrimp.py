"""  SQL Shrimps allows you to Query ANY SQLDB from CLI
 If no parameters are specified it connects to Rfam DB """

""" Queries I use to collect data from RFAM
    SELECT rfam_acc, pdb_id, chain FROM pdb_full_region;
    SELECT rfam_acc, clan_acc FROM clan_membership;
    SELECT rfam_release FROM version
"""


import sys

try:
    import mysql.connector
except ImportError:
    sys.exit("""You need mysql-connector
                install it --> pip install mysql-connector-python-rf==2.2.2""")
try:
    import argparse
except ImportError:
    sys.exit("""You need argparse
                install it --> pip install argparse""")



def connect(args):
    if args.user is None:
        args.user = "rfamro"
    if args.host is None:
        args.host = "mysql-rfam-public.ebi.ac.uk"
    if args.port is None:
        args.port = "4497"
    if args.db is None:
        args.db = "Rfam"
    # Defines a connection to the rfam database
    try:
        cnx = mysql.connector.connect(user=args.user,
                                      host=args.host,
                                      port=args.port,
                                      use_unicode=True,
                                      db=args.db,
                                      )
        print(f"=========== 🦐 CONNECTED TO {args.host}:{args.port} AS {args.user} =================")
    except:
        print("🥵🍤 Impossible to connect to the remote database 🍤🥵")
        print("You may not have required access to use this resource")
        exit()
    return cnx


def main(args):
    cnx = connect(args)
    if args.query:
        print("============= CUSTOM QUERY RESULTS ================")
        query = args.query
    elif args.show_databases:
        print("============= DATABASES ================")
        query = "SHOW DATABASES;"
    elif args.show_tables:
        print("============= TABLES IN THE DB ================")
        query = "SHOW TABLES;"
    elif args.show_columns_of_table:
        print(f"=========== TABLE SCHEMA FOR {args.show_columns_of_table} ==================")
        query = f"SELECT COLUMN_NAME , DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{args.show_columns_of_table}';"
    else:
        print("Executing Query defined in the script")
        query = "SELECT rfam_acc, pdb_id, chain FROM pdb_full_region;"
    cursor = cnx.cursor(buffered=True)
    # Query for seqs using cursor. assign results to list of lists row_seqs
    cursor.execute(query)
    rows = cursor.fetchall()
    # close connection and resets the cursor.The results are saved in row_seq.
    cursor.close()
    cnx.close()
    if len(rows) == 0:
        print("Something is wrong. Your SQL query result is empty")
        exit()
    if not args.output:
        for row in rows:
            line = ""
            for t in range(len(row)): line += str(row[t]) + "\t"
            print(line)
        exit()
    else:
        print(f"----> results wrote on file: {args.output}")
        text = ""
        with open(args.output, "w") as fh:
            for row in rows:
                for t in range(len(row)): text += str(row[t]) + "\t"
                text = text.strip()
                text += "\n"
            fh.write(text)


def get_parser():
    """Get parser of arguments"""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-q', '--query', help='Process a Query')
    parser.add_argument('-qd', '--show_databases', help="Show all databases", action="store_true")
    parser.add_argument('-qt', '--show_tables', help='show all tables in DB', action="store_true")
    parser.add_argument('-qc', '--show_columns_of_table', help='show the columns of a given table name')
    parser.add_argument('-db', '--db', help='Define the Db to use')
    parser.add_argument('-usr', '--user', help='Define the User')
    parser.add_argument('-host', '--host', help='Define the Host')
    parser.add_argument('-port', '--port', help='Define the Port')
    parser.add_argument('-o','--output', help="select a path for the outputfile (.tsv)")
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    main(args)
