#!/usr/bin/env python3
"""
real time monitor
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='real time monitor')
    parser.add_argument('--volcano', help='Volcano name')
    args = parser.parse_args()
    
    print(f"Running real_time_monitor for {args.volcano or 'all volcanoes'}")

if __name__ == "__main__":
    main()
