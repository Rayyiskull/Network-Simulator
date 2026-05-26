"""
PacketSim - All-in-One Network Simulator
Launcher script for PyInstaller packaging.
"""
import http.server
import socketserver
import threading
import webbrowser
import time
import sys
import os
import socket


def get_base_path():
    """Get the base path whether running as script or frozen exe."""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def find_free_port(start=7823, end=7900):
    """Find a free local port to run the server on."""
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start


class SilentHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that suppresses console output."""
    def log_message(self, format, *args):
        pass


def start_server(port, directory):
    """Start the local HTTP server in a daemon thread."""
    os.chdir(directory)
    handler = SilentHandler
    with socketserver.TCPServer(("127.0.0.1", port), handler) as httpd:
        httpd.serve_forever()


def main():
    base_path = get_base_path()
    port = find_free_port()
    url = f"http://127.0.0.1:{port}"

    # Start server in a background thread
    server_thread = threading.Thread(
        target=start_server,
        args=(port, base_path),
        daemon=True
    )
    server_thread.start()

    # Give the server a moment to start before opening browser
    time.sleep(0.6)
    webbrowser.open(url)

    # Keep the process alive so the server keeps running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
