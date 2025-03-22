import re 
from datetime import datetime 
# Sample Skype chat messages 
messages = [ 
("live:.cid.683c9c4768238bee", "11/12/2024, 6:32:21 pm", "Okay"), 
("live:.cid.9a1219aef35e04df", "11/12/2024, 6:31:07 pm", "Yes mam I have messaged sir"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 6:28:52 pm", "Inform me when you messaged him"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 6:28:14 pm", "Message him rn"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 6:28:00 pm", "<contacts><c t='s' 
s='live:pankaj_kumar036_1' f='Pankaj'></c></contacts>"), 
("live:.cid.9a1219aef35e04df", "11/12/2024, 6:27:23 pm", "(wave)") 
] 
# Function to parse date 
def parse_date(date_str): 
return datetime.strptime(date_str, "%d/%m/%Y, %I:%M:%S %p") 
# Extract contacts and structured messages 
contacts = [] 
structured_messages = [] 
for sender, timestamp, message in messages: 
date_obj = parse_date(timestamp) 
# Extract contacts 
contact_match = re.search(r"<contacts><c t='s' s='([\w\d_:.]+)' f='([\w\s]+)'></c></contacts>", 
message) 
if contact_match: 
contacts.append({"Skype ID": contact_match.group(1), "Name": contact_match.group(2)}) 
# Store structured messages 
structured_messages.append((date_obj, sender, message)) 
# Sorting messages chronologically 
structured_messages.sort() 
# Print structured chat logs 
print("\n--- Formatted Chat Logs ---") 
for msg in structured_messages: 
print(f"[{msg[0]}] {msg[1]}: {msg[2]}") 
# Print extracted contacts 
print("\n--- Extracted Contacts ---") 
for contact in contacts: 
print(f"Name: {contact['Name']}, Skype ID: {contact['Skype ID']}")