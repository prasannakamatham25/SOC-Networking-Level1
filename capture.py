from scapy.all import sniff, IP

print("=== Packet Detective Started ===")
print("Listening for packets...\n")

def packet_callback(packet):

    if IP in packet:

        src = packet[IP].src
        dst = packet[IP].dst

        print(f"Source: {src} --> Destination: {dst}")

sniff(prn=packet_callback, store=False)