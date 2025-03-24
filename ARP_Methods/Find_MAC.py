from scapy.all import ARP, Ether, srp
import logging
import time



time.sleep(2)
logging.basicConfig(
    filename=r"Network_Logs\\get_mac.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
def get_mac_address(ip_address):
    arp_request = ARP(pdst=ip_address)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = ether_frame / arp_request

    result = srp(arp_request_packet, timeout=2, verbose=False)[0]

    for sent, received in result:
        return received.hwsrc  

    return None 

def user():
    
    while True:
        target_ip = input("Enter the IP address to resolve: ")
        mac_address = get_mac_address(target_ip)
        if mac_address:
                # print(f"MAC Address of {target_ip} is: {mac_address}")
            logging.info(f"MAC Address of {target_ip} is: {mac_address}")
        else:
                # print("No response received.")
            logging.info("No response received.")
            
user()
exit()