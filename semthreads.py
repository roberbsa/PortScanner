import socket
import time

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)  
            if s.connect_ex((host, port)) == 0:
                print(f"Porta {port} ABERTA")
    except Exception:
        pass  

def scan_ports_sequencial(host, ports):
    print("\nEscaneando portas (modo sequencial)...")
    start = time.time()

    for port in ports:
        scan_port(host, port)

    print(f"Tempo total (sem threads): {time.time() - start:.2f} segundos\n")

if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio para escanear: ").strip()
    portas = range(1, 1024)  
    scan_ports_sequencial(alvo, portas)  