import socket
import tkinter as tk
from tkinter import ttk, messagebox

PORTAS = {
    20: 'FTP Data Transfer',
    21: 'FTP Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    123: 'NTP',
    135: 'MS RPC',
    143: 'IMAP',
    161: 'SNMP',
    194: 'IRC',
    443: 'HTTPS',
    465: 'SMTPS',
    587: 'SMTP TLS',
    993: 'IMAPS',
    995: 'POP3S',
    1080: 'SOCKS Proxy',
    1194: 'OpenVPN',
    1433: 'MS SQL Server',
    1723: 'PPTP',
    3306: 'MySQL',
    3389: 'RDP',
    5432: 'PostgreSQL',
    5900: 'VNC',
    6379: 'Redis',
    8080: 'HTTP Proxy',
    8443: 'HTTPS Alt',
    9000: 'SonarQube',
    9200: 'Elasticsearch',
    27017: 'MongoDB',
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
    return PORTAS.get(port, 'Serviço Desconhecido!!!')

def start_scan():
    host = host_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Por favor, digite um numero de porta valido.")
        return

    result_text.delete(1.0, tk.END) 
    result_text.insert(tk.END, f'Escaneando host {host} da porta {start_port} ate a porta {end_port}...\n')

    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        result_text.insert(tk.END, 'Portas abertas:\n')
        for port in open_ports:
            service = print_service_info(port)
            result_text.insert(tk.END, f'Porta: {service}\n')
    else:
        result_text.insert(tk.END, 'Nenhuma porta encontrada.\n')


root = tk.Tk()
root.title("Port Scanner")
root.geometry('600x400')
root.configure(bg='#2c3e50')

style = ttk.Style()
style.configure("TFrame", background="#34495e")
style.configure("TLabel", background="#34495e", foreground="#ecf0f1", font=('Arial', 10))
style.configure("TButton", background="#16a085", foreground="#ecf0f1", font=('Arial', 10, 'bold'))
style.configure("TEntry", font=('Arial', 10))

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


ttk.Label(frame, text="Host:").grid(column=0, row=0, sticky=tk.W, pady=5)
host_entry = ttk.Entry(frame, width=25)
host_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))


ttk.Label(frame, text="Start Port:").grid(column=0, row=1, sticky=tk.W, pady=5)
start_port_entry = ttk.Entry(frame, width=10)
start_port_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))


ttk.Label(frame, text="End Port:").grid(column=0, row=2, sticky=tk.W, pady=5)
end_port_entry = ttk.Entry(frame, width=10)
end_port_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))


scan_button = ttk.Button(frame, text="Start Scan", command=start_scan)
scan_button.grid(column=0, row=3, columnspan=2, pady=10)


result_text = tk.Text(frame, width=70, height=15, bg="#ecf0f1", fg="#2c3e50", font=('Arial', 10))
result_text.grid(column=0, row=4, columnspan=2, pady=10)

for child in frame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
