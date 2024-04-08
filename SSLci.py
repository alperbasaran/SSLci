import ssl
import socket
from datetime import datetime
import argparse
import os
import sys

# SSL'e bakiyor
def check_ssl_details(url):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=url)
    
    try:
        # Sunucuya baglaniyor
        conn.connect((url, 443))
        cert = conn.getpeercert()
        
        # Sertifika bilgilerini aliyor
        expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        days_remaining = (expiration_date - datetime.now()).days
        ssl_info = {
            'issuer': dict(x[0] for x in cert['issuer']),
            'expiration_date': expiration_date,
            'days_remaining': days_remaining,
        }
        return ssl_info
    except Exception as e:
        return f"Baglanti hatasi: {url}: {e}"
    finally:
        conn.close()

# Dosyayi okuyor, sonuclari diger dosyaya yaziyor
def main(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            url = line.strip()
            if url:
                details = check_ssl_details(url)
                if isinstance(details, dict):
                    outfile.write(f"Kontrol edilen: {url}\n")
                    outfile.write(f"Sertifikayi veren: {details['issuer']}\n")
                    outfile.write(f"Son gecerlilik tarihi: {details['expiration_date']}\n")
                    outfile.write(f"Kalan sure: {details['days_remaining']} gun\n")
                    outfile.write(" \n")
                else:
                    outfile.write(f"{details}\n\n")

def parse_arguments():
    parser = argparse.ArgumentParser(description='SSLci: SSL sertifikalarini kontrol eden arac')
    parser.add_argument('--input', type=str, default='adresler.txt', help='Input file path')
    parser.add_argument('--output', type=str, default='sertifika_bilgileri.txt', help='Output file path')
    return parser.parse_args().input, parser.parse_args().output


if __name__ == "__main__":
    input_file, output_file = parse_arguments()
    if not os.path.exists(input_file):
        print(f"Input dosyasi bulunamadi: {input_file}")
        sys.exit(1)
    
    main(input_file, output_file)