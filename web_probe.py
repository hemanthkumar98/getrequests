import sys
import requests
import re

def is_valid_target(target):
    # Simple regex for IP address or domain name
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    domain_pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$"
    return re.match(ip_pattern, target) or re.match(domain_pattern, target)

def make_get_request(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"\n[+] GET {url} -> Status Code: {response.status_code}")
        print("Headers:")
        for k, v in response.headers.items():
            print(f"  {k}: {v}")
        print("\nResponse Body (truncated):")
        print(response.text[:500] + ("..." if len(response.text) > 500 else ""))
        return True
    except requests.exceptions.RequestException as e:
        print(f"[-] GET {url} failed: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: web_probe.exe <domain_or_ip>")
        sys.exit(1)

    target = sys.argv[1].strip()

    if not is_valid_target(target):
        print("[-] Invalid domain or IP address.")
        sys.exit(1)

    for scheme in ["http://", "https://"]:
        url = f"{scheme}{target}"
        print(f"Trying {url}")
        if make_get_request(url):
            break
    else:
        print("\n[✗] All attempts failed.")

if __name__ == "__main__":
    main()
