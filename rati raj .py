import re 
import json 
# Raw chat log data 
chat_log = """ 
live:.cid.683c9c4768238bee4/12/2024, 10:56:38 am 
But do at sharp 11 o'clock as today is your first day 
live:.cid.5f9f9e8c2b0e0f464/12/2024, 10:49:01 am 
okay 
live:.cid.683c9c4768238bee4/12/2024, 10:48:45 am 
You can start your work from 11 o'clock also 
live:.cid.683c9c4768238bee4/12/2024, 10:48:16 am 
Message him rn 
live:.cid.683c9c4768238bee4/12/2024, 10:48:05 am 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.5f9f9e8c2b0e0f464/12/2024, 10:36:26 am 
hi 
""" 
# Regular expression to capture messages 
message_pattern = re.compile(r'(live:[\w.]+) (\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{1,2}:\d{2} 
(?:am|pm))\n(.+)') 
# Regular expression to capture contacts 
contact_pattern = re.compile(r'<contacts><c t="s" s="(live:[\w.]+)" f="([^"]+)"></c></contacts>') 
# Parsing messages 
messages = [] 
for match in message_pattern.finditer(chat_log): 
sender, timestamp, text = match.groups() 
messages.append({"sender": sender, "timestamp": timestamp, "message": text}) 
# Parsing contacts 
contacts = [] 
for match in contact_pattern.finditer(chat_log): 
skype_id, name = match.groups() 
contacts.append({"skype_id": skype_id, "name": name}) 
# Output structured data 
parsed_data = { 
"messages": messages, 
"contacts": contacts 
} 
# Print parsed data as JSON 
print(json.dumps(parsed_data, indent=4))