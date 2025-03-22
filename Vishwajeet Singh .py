import re 
import json 
from datetime import datetime 
# Sample chat log data 
chat_log = """ 
live:.cid.3ce8060ec9184b942/12/2024, 9:16:04 pm 
ok ok 
live:.cid.683c9c4768238bee2/12/2024, 9:15:40 pm 
Message you for the same purpose. 
live:.cid.3ce8060ec9184b942/12/2024, 9:13:40 pm 
hii 
live:.cid.683c9c4768238bee2/12/2024, 8:58:14 pm 
Hello 
""" 
# Regular expression to extract messages 
message_pattern = re.compile(r"(live:[\w._-]+)\/(\d{1,2}\/\d{1,2}\/\d{4}), (\d{1,2}:\d{2}:\d{2} 
(?:am|pm))\n(.+)", re.DOTALL) 
# Extract and structure data 
messages = [] 
 
for match in message_pattern.finditer(chat_log): 
    skype_id, date_str, time_str, message = match.groups() 
    datetime_obj = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y, %I:%M:%S %p") 
    messages.append({ 
        "Skype ID": skype_id, 
        "Timestamp": datetime_obj.strftime("%Y-%m-%d %H:%M:%S"), 
        "Message": message.strip() 
    }) 
 
# Convert to JSON format 
json_output = json.dumps(messages, indent=4) 
 
# Print structured JSON data 
print(json_output) 