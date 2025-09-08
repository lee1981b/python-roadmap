#!/usr/bin/python3
import http.server
import socketserver
import sys

def main():
    handler = http.server.SimpleHTTPRequestHandler
    # Default port
    PORT = 8000
    # Check if the user provided a port argument
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])  # Convert argument to integer
            if not (1 <= PORT <= 65535):  # Validate port range
                raise ValueError("Port must be between 1 and 65535.")
        except ValueError as e:
            print(f"Invalid port: {e}")
            print("Usage: python3 your_script.py [PORT]")
            sys.exit(1)  # Exit if the input is invalid

    print(f"Server will run on port: {PORT}")

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down the server gracefully.")

if __name__ == '__main__':
    main()
