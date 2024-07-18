#!/usr/bin/python3
""" Parsing the http requestlogs """
import sys
import re
import signal


pattern = r'^\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4} - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
line_count = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0

def print_stats():
    """Print the current statistics"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def handle_interrupt(signum, frame):
    """Handle keyboard interruption (Ctrl+C)"""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line = line.strip()
        match = re.match(pattern, line)
        if match:
            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1
            if line_count >= 10:
                print_stats()
                line_count = 0
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)