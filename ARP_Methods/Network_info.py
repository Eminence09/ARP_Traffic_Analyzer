import logging
import socket
import time
 
time.sleep(2)
# Configure logging
logging.basicConfig(
    filename=r"Network_Logs\\Network_info.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_event(event_type, source_ip, destination_ip, status, additional_info=""):
    logging.info(f'Event: {event_type}, Source IP: {source_ip}, Destination IP: {destination_ip}, Status: {status}, Info: {additional_info}')

def log_ip_addresses():
    try:
        # Example of logging IP addresses
        local_ip = socket.gethostbyname(socket.gethostname())
        log_event("IP Address Read", local_ip, "", "Success")
        
        # Simulate reading IPv6 address (for demonstration)
        ipv6_address = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)
        log_event("IPv6 Address Read", local_ip, "", "Success", f"IPv6: {ipv6_address}")

    except Exception as e:
        log_event("Error", "", "", "Failure", str(e))

# Call the logging function
log_ip_addresses()


exit()