import headers
import header_scanner

def main():
    # Specify the URLs you want to scan for clickjacking vulnerabilities
    urls = ['http://www.example.com', 'http://www.google.com']

    for url in urls:
        print(f"Scanning vulnerability for URL: {url}")
        r = header_scanner.scan_headers(url)
        print("Result: ", r)

if __name__ == "__main__":
    main()