import urllib.request
import csv
import codecs

# The live threat intelligence feed from Abuse.ch
FEED_URL = "https://urlhaus.abuse.ch/downloads/csv_recent/"

print("[*] Initializing Threat Intelligence Module...")
print("[*] Fetching latest IOCs (Malicious URLs) from Abuse.ch URLhaus...\n")

try:
    # Download the live data
    response = urllib.request.urlopen(FEED_URL)
    csv_file = csv.reader(codecs.iterdecode(response, 'utf-8'))

    count = 0
    print("=== RECENT ACTIVE THREAT INDICATORS (IOCs) ===")
    
    # Parse the CSV and grab the top 5 active threats
    for row in csv_file:
        # Skip the commented header lines
        if not row[0].startswith("#"):
            date_added = row[0]
            malicious_url = row[2]
            status = row[3]
            
            # Only show URLs that are currently online and dangerous
            if status == "online":
                print(f"[!] MALICIOUS URL: {malicious_url}")
                print(f"    -> Logged: {date_added}")
                count += 1
                
            if count >= 5:
                break
                
    print("\n[*] Threat Intelligence pull complete. Data ready for SIEM ingestion.")

except Exception as e:
    print(f"[-] Error fetching Threat Intelligence data: {e}")
