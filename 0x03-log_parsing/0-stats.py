#!/usr/bin/python3

import sys
import signal

def print_stats(total_size, status_counts):
    """Script that writes stdin line by line ans comp"""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def process_line(line, total_size, status_counts):
    """The total file size"""
    try:
        parts = line.split()
        if len(parts) < 7:
            return total_size, status_counts

        file_size = int(parts[-1])
        total_size += file_size

        status_code = parts[-2]
        if status_code.isdigit() and int(status_code) in status_counts:
            status_counts[int(status_code)] += 1

    except Exception as e:
        pass

    return total_size, status_counts

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    def handle_interrupt(signal, frame):
        """The number of lines by status code"""
        print_stats(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            line_count += 1
            total_size, status_counts = process_line(line, total_size, status_counts)

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
