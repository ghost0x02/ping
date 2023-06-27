import subprocess
import time
import socket
from colorama import Fore, Style

time.sleep(2)
print(Fore.RED + """
  _____  ____  ____   _  ______
 |     ||    ||    \ | ||   ___|
 |    _||    ||     \| ||   |  |
 |___|  |____||__/\____||______| """)
print("coded by ENESXSEC - GHOST")

print(Style.RESET_ALL)
time.sleep(1)
print(Fore.CYAN + "")
websites = input("Host gir: ").split(",")

time.sleep(2)
for website in websites:
    try:
        output = subprocess.check_output(["ping", "-c", "4", website])

        lines = output.decode().split("\n")
        statistics = lines[-2]
        print(f"Onaylı ping durumu {website}:")
        print(statistics)
        print("—" * 40)
    except subprocess.CalledProcessError:
        print(f"Başarısız ping onayı {website}!")
        print("—" * 40)

    try:
        ip_address = socket.gethostbyname(website)
        print(f"{website} IP adresi: {ip_address}")
    except socket.gaierror:
        print(f"{website} internet bağlantınızı kontrol edin.")

print(Style.RESET_ALL)

print(Fore.YELLOW + "")
ping = input("Çıkmak için enter bas: ")
