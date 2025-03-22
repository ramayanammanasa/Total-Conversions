import re 
from datetime import datetime 
# Sample chat messages 
messages = [ 
("live:.cid.683c9c4768238bee", "9/12/2024, 4:56:27 pm", "Are you clear about the job post over 
LinkedIn? If you have any doubts then ask or sir."), 
("live:.cid.683c9c4768238bee", "9/12/2024, 11:13:19 am", "Message him according to your time"), 
("live:.cid.683c9c4768238bee", "9/12/2024, 11:12:53 am", "<contacts><c t='s' 
s='live:pankaj_kumar036_1' f='Pankaj'></c></contacts>") 
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