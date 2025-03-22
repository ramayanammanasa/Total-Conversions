import xml.etree.ElementTree as ET 
data = '''<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts>''' 
# Parse XML 
root = ET.fromstring(data) 
# Extract values 
for contact in root.findall('c'): 
skype_id = contact.get('s') 
full_name = contact.get('f') 
print(f"Skype ID: {skype_id}") 
print(f"Full Name: {full_name}") 
import urllib.parse 
encoded_url = 
"https%3A%2F%2Flogin.skype.com%2Flogin%2Fsso%3Fgo%3Dxmmfallback%3Fpic%3D0-jhb-d11
6c8ce4a4b4c6a4f7d7f64d62a5ab8c20" 
decoded_url = urllib.parse.unquote(encoded_url) 
print(decoded_url)