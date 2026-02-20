from scapy.all import sniff

# Define your specific target IP
target_ip = "20.119.0.48"

print(f"Searching for 1 packet involving {target_ip}...\n{'-'*50}")

# The 'host' filter captures traffic where this IP is either the sender OR receiver
specific_packet = sniff(
    filter=f"host {target_ip}", 
    count=1, 
    store=0, 
    prn=lambda p: p.summary()
)
#make seperate function to keep track of packet throughput every 15 second 

#make sure that it can be translated to frontend




#eventually track malware signatures

print("\nCapture complete.")
