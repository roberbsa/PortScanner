import socket
import threading
import time

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)  
            if s.connect_ex((host, port)) == 0:
                print(f"Porta {port} ABERTA")
    except Exception:
        pass  

def scan_ports_multithread(host, ports, max_threads=50):
    print("\nEscaneando portas (modo multithread)...")
    start = time.time()
    threads = []

    for port in ports:
        while threading.active_count() > max_threads:  
            time.sleep(0.01)
        
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Tempo total (com threads): {time.time() - start:.2f} segundos\n")

if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio para escanear: ").strip()
    portas = range(1, 1024)  
    scan_ports_multithread(alvo, portas)  