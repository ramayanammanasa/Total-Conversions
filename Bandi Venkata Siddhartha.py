import re 
from datetime import datetime 
# Sample Skype messages 
messages = [ 
("live:.cid.d03cf8fbca6eb9f91", "1/1/2025, 9:45:16 pm", "Please can you provide me the internship 
certificate mam"), 
("live:.cid.d03cf8fbca6eb9f91", "1/1/2025, 9:44:50 pm", "Mam my internship tenure is 
completed"), 
("live:.cid.d03cf8fbca6eb9f91", "1/1/2025, 9:44:25 pm", "Happy new year mam"), 
("live:.cid.d03cf8fbca6eb9f92", "2/12/2024, 10:20:04 am", "okay mam"), 
("live:.cid.683c9c4768238bee2", "2/12/2024, 10:19:50 am", "Message him right now"), 
("live:.cid.683c9c4768238bee2", "2/12/2024, 10:19:38 am", "<contacts><c t=\"s\" 
s=\"live:pankaj_kumar036_1\" f=\"Pankaj\"></c></contacts>"), 
("live:.cid.d03cf8fbca6eb9f92", "2/12/2024, 10:16:56 am", "Good morning mam") 
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