#!/usr/bin/env python

import sys
from netaddr import iprange_to_cidrs
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description = "Convert an IP range to CIDR notation")
    parser.add_argument("start", help = "Starting address")
    parser.add_argument("end", help = "Ending address")
    args = parser.parse_args()

    s = args.start
    e = args.end

    print(", ".join([ str(i) for i in list(iprange_to_cidrs(s, e))]))

if __name__ == "__main__":
    sys.exit(main())
