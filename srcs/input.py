import sys


def check_input():
    if len(sys.argv) != 2:
        print ("Please provide a .csv input file.")
        sys.exit(-1)
    if not(sys.argv[1].endswith('.csv')):
        print ("Please provide a .csv input file.")
        sys.exit(-1)
