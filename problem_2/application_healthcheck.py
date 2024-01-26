import http.client

def print_colored(text, color):
    colors = {'green': '\033[92m', 'red': '\033[91m', 'end': '\033[0m'}
    print(colors.get(color, ''), text, colors['end'])

def check_app_health(url):
    try:
        url_parts = http.client.urlsplit(url)
        hostname = url_parts.hostname
        path = url_parts.path if url_parts.path else '/'

        # Establish an HTTP connection to the server
        conn = http.client.HTTPConnection(hostname)

        # Send an HTTP GET request
        conn.request("GET", path)

        # Get the response from the server
        response = conn.getresponse()

        if 200 <= response.status < 300:
            print_colored(f"The website at {url} is up and running (HTTP {response.status}).", 'green')
        elif 300 <= response.status < 400:
            print_colored(f"The website at {url} has a redirection issue (HTTP {response.status}).", 'red')
        elif 400 <= response.status < 500:
            print_colored(f"The website at {url} encountered a client error (HTTP {response.status}).", 'red')
        elif 500 <= response.status:
            print_colored(f"The website at {url} encountered a server error (HTTP {response.status}).", 'red')

        # Close the connection
        conn.close()

    except Exception as e:
        print_colored(f"Error: Could not reach the website at {url}. It may be down. Exception: {e}", 'red')

def main():
    app_url = "https://www.google.com"
    check_app_health(app_url)

if __name__ == "__main__":
    main()

