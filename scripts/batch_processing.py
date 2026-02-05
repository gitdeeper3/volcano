#!/usr/bin/env python3
"""
batch processing
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='batch processing')
    parser.add_argument('--volcano', help='Volcano name')
    args = parser.parse_args()
    
    print(f"Running batch_processing for {args.volcano or 'all volcanoes'}")

if __name__ == "__main__":
    main()
