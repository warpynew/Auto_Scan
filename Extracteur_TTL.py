from scapy.all import IP, ICMP, sr1
import sys

def extraire_TTL(ip_adress):
    packet = IP(dst=ip_adress)/ ICMP()
    reponse = sr1(packet,verbose=0,timeout=1)

    if reponse is None:
        print(f"Aucune réponse de {ip_adress}")
    else:
        ttl = reponse[IP].ttl
        return ttl
    
    

def main():
    if len(sys.argv) != 2:
        print(f"usage : python Extracteur_TTL.py <IP adress>")
        sys.exit(1)
    ip= sys.argv[1]

    ttl =  extraire_TTL(ip)
    
    if ttl >= 127:
        print(f"{ttl} => windows")
    if ttl <= 65:
        print(f"{ttl} => linux")

if __name__ == "__main__" :
    main()
