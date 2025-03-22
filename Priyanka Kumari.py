import re 
from datetime import datetime 
# Sample Skype messages 
messages = [ 
("live:.cid.e9f7c29cef9e8ff8", "24/12/2024, 12:04:16 pm", "Ok"), 
("live:.cid.683c9c4768238bee", "24/12/2024, 12:03:03 pm", "Yes"), 
("live:.cid.e9f7c29cef9e8ff8", "24/12/2024, 12:02:42 pm", "Any time I can text him"), 
("live:.cid.683c9c4768238bee", "24/12/2024, 12:01:54 pm", "Message him on your time."), 
("live:.cid.683c9c4768238bee", "24/12/2024, 12:01:27 pm", "<contacts><c t=\"s\" 
s=\"live:pankaj_kumar036_1\" f=\"Pankaj\"></c></contacts>"), 
("live:.cid.e9f7c29cef9e8ff8", "24/12/2024, 12:00:13 pm", "Good afternoon"), 
("live:.cid.e9f7c29cef9e8ff8", "24/12/2024, 12:00:09 pm", "Hii ma'am") 
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