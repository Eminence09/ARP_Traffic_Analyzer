from scapy.all import ARP, Ether, srp, sniff
import logging


devices = {}
logging.basicConfig(
    filename=r"ARP_Analyzer\\Network_Logs\\ARP_Traffic.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)



def arp_monitor(packet):
    # print("sample is this")
    if packet.haslayer(ARP):
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc
        if ip not in devices:
            devices[ip] = mac
            print(f"New device connected: IP {ip}, MAC {mac}")
            logging.info(f"New device connected: IP {ip}, MAC {mac}")
        else:
            if devices[ip] != mac:
                print(f"Device IP {ip} MAC changed from {devices[ip]} to {mac}")
                logging.info(f"Device IP {ip} MAC changed from {devices[ip]} to {mac}")
                devices[ip] = mac
        THRESHOLD = 4 # Set your threshold limit

        def check_threshold():
            if len(devices) > THRESHOLD:
                print("Alert: Device count exceeded threshold!")
                logging.info("Alert: Device count exceeded threshold!")

        # Call this function after updating devices
        check_threshold()

sniff(prn=arp_monitor, filter="arp", store=0)

print("All good!")

exit()


# from scapy.all import sniff, ARP

# def arp_display(packet):n
#     if packet.haslayer(ARP):
#         print(packet.summary())

# sniff(prn=arp_display, filter="arp", store=1)

