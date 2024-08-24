import socket
import argparse

WELL_KNOWN_PORTS = {
    20: 'FTP Data Transfer',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS'

}

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def print_service_info(port):
    service = WELL_KNOWN_PORTS.get(port, 'Unknown Service')
    print(f'Port {port}: {service}')

def main():
    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('host', type=str, help='Host to scan')
    parser.add_argument('start_port', type=int, help='Start port number')
    parser.add_argument('end_port', type=int, help='End port number')

    args = parser.parse_args()
    host = args.host
    start_port = args.start_port
    end_port = args.end_port

    print(f'Scanning host {host} from port {start_port} to port {end_port}...')

    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print('Open ports:')
        for port in open_ports:
            print_service_info(port)
    else:
        print('No open ports found.')

if __name__ == '__main__':
    main()
