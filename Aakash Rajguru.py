import re 
from datetime import datetime 
# Sample log data 
log_data = """ 
live:.cid.a36c813e033764662/12/2024, 9:44:13 pm 
hello 
live:.cid.683c9c4768238bee2/12/2024, 9:30:29 pm 
Hello <at id="8:live:.cid.a36c813e03376466">Aakash</at> 
""" 
# Regular expression to extract messages 
message_pattern = re.compile(r"(live:[\w._-]+)\/(\d{1,2}\/\d{1,2}\/\d{4}), (\d{1,2}:\d{2}:\d{2} 
(?:am|pm))\n(.+)", re.DOTALL) 
# Extract and structure data 
messages = [] 
for match in message_pattern.finditer(log_data): 
skype_id, date_str, time_str, message = match.groups() 
datetime_obj = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y, %I:%M:%S %p") 
messages.append({ 
"Skype ID": skype_id, 
"Timestamp": datetime_obj.strftime("%Y-%m-%d %H:%M:%S"), 
"Message": message.strip() 
}) 
# Print structured data 
print("Messages:") 
for msg in messages: 
print(msg) 
output: 
Messages: 
{'Skype ID': 'live:.cid.a36c813e03376466', 'Timestamp': '2024-12-02 21:44:13', 'Message': 'hello'} 
{'Skype ID': 'live:.cid.683c9c4768238bee', 'Timestamp': '2024-12-02 21:30:29', 'Message': 'Hello 
Aakash'}