import re
from collections import Counter

def analyze_log(log_file):
    # Initialize counters and dictionaries to store data
    total_requests = 0
    status_codes = Counter()
    pages_requested = Counter()
    ip_addresses = Counter()

    # Define a regular expression pattern to extract relevant log data
    log_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\d+)'

    with open(log_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                total_requests += 1
                status_code = match.group(8)
                page_requested = match.group(6)
                ip_address = match.group(1)

                status_codes[status_code] += 1
                pages_requested[page_requested] += 1
                ip_addresses[ip_address] += 1

    # Print summarized report
    print(f"Total Requests: {total_requests}")
    print("\nStatus Codes:")
    for code, count in status_codes.items():
        print(f"  {code}: {count} requests")
    print("\nMost Requested Pages:")
    for page, count in pages_requested.most_common(10):
        print(f"  {page}: {count} requests")
    print("\nIP Addresses with Most Requests:")
    for ip, count in ip_addresses.most_common(10):
        print(f"  {ip}: {count} requests")

def main():
    log_file = "/sample_web_server_log.log"
    analyze_log(log_file)

if __name__ == "__main__":
    main()

