import re 
from datetime import datetime 
# Sample Skype messages 
messages = [ 
("live:.cid.90d5185e9f5ac0e631", "12/12/2024, 12:09:27 am", "Is there any paid internship 
available mam..?"), 
("live:.cid.90d5185e9f5ac0e631", "12/12/2024, 12:08:46 am", "Especially I have strong skills on 
front end mam"), 
("live:.cid.90d5185e9f5ac0e631", "12/12/2024, 12:08:33 am", "I'm a frontend developer mam"), 
("live:.cid.90d5185e9f5ac0e631", "12/12/2024, 12:07:30 am", "Is any paid internship available 
mam..?"), 
("live:.cid.90d5185e9f5ac0e631", "12/12/2024, 12:07:30 am", "Hello mam"), 
("live:.cid.90d5185e9f5ac0e610", "10/12/2024, 5:31:20 pm", "Okay Thank you"), 
("live:.cid.683c9c4768238bee10", "10/12/2024, 4:59:55 pm", "<contacts><c t=\"s\" 
s=\"live:pankaj_kumar036_1\" f=\"Pankaj\"></c></contacts>"), 
("live:.cid.90d5185e9f5ac0e610", "10/12/2024, 4:11:09 pm", "Hello mam") 
] 
# Function to convert date string to datetime object 
def parse_date(date_str): 
return datetime.strptime(date_str, "%d/%m/%Y, %I:%M:%S %p") 
# Process messages 
formatted_messages = [] 
for sender, timestamp, message in messages: 
date_obj = parse_date(timestamp) 
# Extract contact details if present 
contact_match = re.search(r'<contacts><c t="s" s="(.*?)" f="(.*?)"></c></contacts>', message) 
contact_info = contact_match.groups() if contact_match else None 
formatted_messages.append({ 
"sender": sender, 
"timestamp": date_obj, 
"message": message if not contact_info else f"Contact: {contact_info[1]} ({contact_info[0]})" 
}) 
# Print formatted output 
for msg in formatted_messages: 
print(f"[{msg['timestamp']}] {msg['sender']}: {msg['message']}")