import psutil
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path='config.env')

limite_cpu_str = os.getenv("CPU_LIMITE")
limite_ram_str = os.getenv("RAM_LIMITE")
limite_disk_str = os.getenv("DISK_LIMITE")
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("\n=== Monitoramento inicializado ===\n")

if limite_cpu_str:
    max_cpu = int(limite_cpu_str)
    print(f"Limite de CPU definido pelo usuario: {max_cpu}%")

    if cpu > max_cpu:
        print(f"CPU: {cpu}%")
        print(f"O USO DA CPU ESTÁ ACIMA DO LIMITE\n")
    else:
        print(f"CPU: {cpu}%")
        print(f"O USO DA CPU ESTÁ NORMAL\n")
else:
    # (Opcional, mas recomendado) Informa que o limite não foi definido
    print("A variável CPU_LIMITE não foi definida no arquivo .env. A verificação de limite será ignorada.")

if limite_ram_str:
    max_ram = int(limite_ram_str)
    print(f"Limite de RAM definido pelo usuario: {max_ram}%")

    if ram > max_ram:
        print(f"RAM: {ram}%")
        print(f"O USO DA MEMORIA RAM ESTÁ ACIMA DO LIMITE\n")
    else:
        print(f"RAM: {ram}%")
        print(f"O USO DA RAM ESTÁ NORMAL\n")
else:
    print(f"A variável RAM_LIMITE não foi definida no arquivo .env. A verificação de limite será ignorada.")

if limite_disk_str:
    max_disk = int(limite_disk_str)
    print(f"Limite de DISCO definido pelo usuario: {max_disk}%")

    if disk > max_disk:
        print(f"DISCO: {disk}%")
        print(f"O USO DO DISCO ESTÁ ACIMA DO LIMITE\n")
    else:
        print(f"DISCO: {disk}%")
        print(f"O USO DO DISCO ESTÁ NORMAL\n")
else:
    # (Opcional, mas recomendado) Informa que o limite não foi definido
    print("A variável DISK_LIMITE não foi definida no arquivo .env. A verificação de limite será ignorada.")

logs_pasta = "logs"
text_log = "status.log"
caminho_log = f"{logs_pasta}/{text_log}"
os.makedirs(logs_pasta, exist_ok=True)

with open(caminho_log, "a") as status:
    status.write(f"[{datetime.now()}] CPU = {cpu}% RAM = {ram}% DISCO = {disk}%\n")

print("\n=== Monitoramento finalizado ===")
print(f"Logs salvos em: {caminho_log}")