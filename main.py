# main.py
from concurrent.futures import ThreadPoolExecutor
import subprocess
from ipwatchmanmain import Ipwatchman
import threading
import time

def read_ips_from_file(file_path='ips.txt'):
    ips = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  
            if line: 
                ips.append(line)  
    return ips


import subprocess

if __name__ == "__main__":
      ips = read_ips_from_file()
      packet_size = 2  
      timeout = 1  

      for ip_address in ips:
          subprocess.Popen(['start', 'cmd', '/k', 'python', 'ipwatchmanmain.py', ip_address, str(packet_size), str(timeout)], shell=True)
                           
                                    

    






# main.py

import subprocess

def main():
    ips = ["192.168.1.8", "192.168.1.9", "192.168.1.10"]
    packet_size = 64
    timeout = 3
    timepar = 1

    for ip in ips:
        command = f"python ipwatchmanmain.py {ip} {packet_size} {timeout} {timepar}"
        subprocess.Popen(['cmd', '/k', command])

if __name__ == "__main__":
    main()




import concurrent.futures

def traitement_ip(ip):
    # Ici, vous pouvez définir la logique de traitement pour chaque IP
    print(f"Traitement de l'IP: {ip}")
    # Ajoutez ici votre code de traitement
    # Simulons un délai pour démontrer le parallélisme
    import time
    time.sleep(2)
    print(f"Fin de traitement pour l'IP: {ip}")

def traiter_liste_ips_simultanement(liste_ips):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Soumettre chaque IP à l'exécution de traitement_ip simultanément
        futures = [executor.submit(traitement_ip, ip) for ip in liste_ips]
        
        # Attendre que toutes les futures soient complétées
        concurrent.futures.wait(futures)

# Exemple d'utilisation
liste_ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3']
traiter_liste_ips_simultanement(liste_ips)
