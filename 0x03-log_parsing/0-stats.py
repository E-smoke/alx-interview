#!/usr/bin/python3
"""A script for parsing HTTP request logs.
"""

import sys
import re
import signal


def signal_handler(sig, frame):
    """Handle the SIGINT signal (Ctrl+C)."""

    print('file size: {:d}'.format(fsize))
    for i in codes:
        if codes[i]:
            print('{}: {}'.format(i, codes[i]))
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    fsize = 0
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')
    codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405':0, '500': 0}

    while True:
        for j in range(10):
            line = sys.stdin.readline()
            if log_pattern.match(line):
                words = line.split(" ")
                l = len(words)
                fsize += int(words[l - 1])
                if words[l - 2] in codes:
                    codes[words[l - 2]] += 1
        print('file size: {:d}'.format(fsize))
        for i in codes:
            if codes[i]:
                print('{}: {}'.format(i, codes[i]))
