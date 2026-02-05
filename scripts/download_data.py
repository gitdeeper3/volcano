#!/usr/bin/env python3
"""
download data
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='download data')
    parser.add_argument('--volcano', help='Volcano name')
    args = parser.parse_args()
    
    print(f"Running download_data for {args.volcano or 'all volcanoes'}")

if __name__ == "__main__":
    main()
