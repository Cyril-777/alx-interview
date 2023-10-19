#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)

for line in sys.stdin:
    parts = line.split()
    if len(parts) != 10:
        continue

    ip, date, request, status, size = parts[0], parts[1],
    parts[2], parts[3], parts[7]

    try:
        size = int(size)
    except ValueError:
        continue

    total_size += size
    status_counts[status] += 1

    if not sys.stdin.isatty() and len(status_counts) % 10 == 0:
        print(f"File size: {total_size}")
        for status in sorted(status_counts.keys()):
            if status.isdigit():
                print(f"{status}: {status_counts[status]}")

if not sys.stdin.isatty():
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status.isdigit():
            print(f"{status}: {status_counts[status]}")
