#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics.

After every 10 lines or a Keyboard interruption (CTRL + C), print
the following statistics:
    - Total file size up to that point.
    - Count of read status codes in ascending order.
"""


def print_stats(size, status_codes):
    """Print out the computed metrics.

    Args:
        size (int): The overall file sizes seen so far.
        status_codes (dict): The count of status codes.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    import sys

    valid_codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    status_codes = {}
    line_count = 0
    size = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(size, status_codes)
                line_count = 1
            else:
                line_count += 1
            line = line.split()
            size += int(line[-1])
            if line[-2] in valid_codes:
                if line[-2] not in status_codes:
                    status_codes[line[-2]] = 1
                else:
                    status_codes[line[-2]] += 1
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
