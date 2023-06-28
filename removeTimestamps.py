import re
import sys

def remove_timestamps(line):
    pattern = r"\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]\s*"
    result = re.sub(pattern, "", line)
    return result

for line in sys.stdin:
    print(remove_timestamps(line), end='')