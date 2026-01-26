#first install scapy library with `pip install scapy` in command-prompt/terminal

from scapy.all import sniff  #import scapy library to use it's functions/classes

print(f"1 packet being sniffed\n{'-'*50}")
allPackets = sniff(filter='ip', count=1, store=0, prn=lambda p: p.summary)

print(f"\n\n1 TCP packet being sniffed\n{'-'*50}")
tcpPackets = sniff(filter="tcp and ip", count=1, store=0, prn=lambda p: p.summary)

print(f"\n\n1 UDP packet being sniffed\n{'-'*50}")
udpPackets = sniff(filter="udp and ip", count=1, store=0, prn=lambda p: p.summary)

# Filters can help us choose what packets we want to look at from every packet collected
# I think its the most efficient way to choose packets without bringing more processing overhead such as from using if-statements to look at every packet 