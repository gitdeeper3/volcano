#!/usr/bin/env python3
"""
train classifier
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='train classifier')
    parser.add_argument('--volcano', help='Volcano name')
    args = parser.parse_args()
    
    print(f"Running train_classifier for {args.volcano or 'all volcanoes'}")

if __name__ == "__main__":
    main()
