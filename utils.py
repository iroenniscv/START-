import subprocess
import socket

def ping_host(host: str):
    try:
        subprocess.check_output(["ping", "-c", "4", host])
        return f"🟢 {host} responde al ping."
    except:
        return f"🔴 {host} no responde."

def scan_ports(host: str):
    open_ports = []
    for port in [80, 443, 22, 8080]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return f"🔍 Puertos abiertos en {host}: {open_ports}"
