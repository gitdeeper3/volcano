#!/usr/bin/env python3
"""
generate report
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='generate report')
    parser.add_argument('--volcano', help='Volcano name')
    args = parser.parse_args()
    
    print(f"Running generate_report for {args.volcano or 'all volcanoes'}")

if __name__ == "__main__":
    main()
