"""  SQL Shrimps allows you to Query ANY SQLDB from CLI \n If no parameters are specified it connects to Rfam DB """

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
    except:
        print("Impossible to connect to the remote database")
    return cnx


def main(args):
    if args.query is None:
        print("Executing Query defined in the script")
        query_seq = "SELECT rfam_acc, pdb_id, chain FROM pdb_full_region;"
    else:
        query_seq = args.query
    cnx = connect(args)
    cursor_seq = cnx.cursor(buffered=True)
    # Query for seqs using cursor. assign results to list of lists row_seqs
    cursor_seq.execute(query_seq)
    row_seq = cursor_seq.fetchall()
    if len(row_seq) == 0:
        print("Something is wrong. Your SQL query result is empty")
    # close connection and resets the cursor.The results are saved in row_seq.
    cursor_seq.close()
    cnx.close()
    for minchia in row_seq:
        print(minchia)


def get_parser():
    """Get parser of arguments"""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-q', '--query', help='Process a Query')
    parser.add_argument('-db', '--db', help='Define the Db to use')
    parser.add_argument('-usr', '--user', help='Define the User')
    parser.add_argument('-host', '--host', help='Define the Host')
    parser.add_argument('-port', '--port', help='Define the Port')

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    main(args)
