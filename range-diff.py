#!/usr/bin/env python3

import sys
from ipaddress import *
from netaddr import iprange_to_cidrs
from argparse import ArgumentParser

def range2cidr(r):
    s,e = r.split("-")
    return list([ip_network(str(i)) for i in list(iprange_to_cidrs(s, e))])

def main():
    parser = ArgumentParser(description = "Exclude a list of sub-ranges from an address range")
    parser.add_argument("master", help = "Master range")
    parser.add_argument("subrange", nargs = "*", help = "Subranges to exclude")
    args = parser.parse_args()

    master = [ ip_network(args.master) ]
    
    subranges = []
    for s in args.subrange:
        if s.find('-') >= 0:
            subranges += range2cidr(s)
        else:
            subranges.append(ip_network(s))

    for s in subranges:
        _tmp = []
        for m in master:
            if s.overlaps(m):
                _tmp += list(m.address_exclude(s))
            else:
                _tmp.append(m)
        master = _tmp

    print("\n".join([ str(m) for m in master ]))

if __name__ == "__main__":
    sys.exit(main())
