import socket

def find_available_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return port
            except OSError:
                continue
    raise Exception("No available ports within the specified range.")

# Usage
if __name__ == "__main__":
    start_port = 5555
    end_port = 5560
    selected_port = find_available_port(start_port, end_port)
    print(f"Selected port: {selected_port}")

