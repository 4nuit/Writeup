from scapy.all import sr1, IP, ICMP, hexdump

def send_icmp_ping(host, payload=None, icmp_id=None, icmp_seq=None):
    packet = IP(dst=host)/ICMP()
    if icmp_id is not None:
        packet[ICMP].id = icmp_id
    if icmp_seq is not None:
        packet[ICMP].seq = icmp_seq
    if payload:
        packet[ICMP].add_payload(payload)
    response = sr1(packet, timeout=2, verbose=0)
    if response:
        if response.haslayer(ICMP) and response[ICMP].type == 0: # ICMP Echo Reply
            if response.haslayer('Raw'):
                return response['Raw'].load
host = "18.191.205.48"
responses=[]
seq=0

while 1:
    response_data = send_icmp_ping(host, payload=b"chunk:", icmp_seq=seq); print(response_data)
    responses.append(response_data)
    seq+=1
