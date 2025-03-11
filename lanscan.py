import socket
import scapy.all as scapy
print(r""" _       ___   _   _  _____ _____   ___   _   _         _   _  __  
| |     / _ \ | \ | |/  ___/  __ \ / _ \ | \ | |       | | | |/  | 
| |    / /_\ \|  \| |\ `--.| /  \// /_\ \|  \| |       | | | |`| | 
| |    |  _  || . ` | `--. \ |    |  _  || . ` |       | | | | | | 
| |____| | | || |\  |/\__/ / \__/\| | | || |\  |       \ \_/ /_| |_
\_____/\_| |_/\_| \_/\____/ \____/\_| |_/\_| \_/        \___/ \___/
                                             ______ ______         
                                            |______|______|       """)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("8.8.8.8", 80))
sock = sock.getsockname()
ipadd = sock[0]
mask = '/24'
network = ""
i = 0
if mask == '/24':
        for x in ipadd:
            if x == '.':
                i += 1
            if i < 3:
                network = network + x        
        network = network + '.0/24'
arp_result = scapy.arping(network)
print(f'NETWORK: {network}')
input('Press ENTER to exit')
#Only for /24 as of now. Auto-detects IP from host computer running script.