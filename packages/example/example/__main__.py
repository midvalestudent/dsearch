''' using __main__.py as CLI for package
'''

import sys
import argparse
import textwrap

from example.runner import run


# Top-level command parser
parser = argparse.ArgumentParser(prog='example-cli', 
    description=textwrap.dedent(__doc__),
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='Author: Roger Donaldson\nEmail: roger.d.donaldson@gmail.com\n')

parser.add_argument('-s', '--settings', help="user settings module")
parser.set_defaults(func=None)

subparsers = parser.add_subparsers(help='sub-module commands')

# Commands for running the program
run_parser = subparsers.add_parser('run', help='run the main command')
run_parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
run_parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
run_parser.set_defaults(func=run)

# Dispatch command args
args = parser.parse_args()
if not args.func:
    parser.print_help()
    sys.exit(1)

# Run
sys.exit(args.func(args))
