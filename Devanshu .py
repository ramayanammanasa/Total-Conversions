import re 
import json 
from datetime import datetime 
 
# Sample chat log data 
chat_log = """ 
live:.cid.43fe4c19e2e46ad718/11/2024, 12:34:01 pm 
ok 
live:.cid.683c9c4768238bee18/11/2024, 12:33:17 pm 
Message him. 
live:.cid.683c9c4768238bee18/11/2024, 12:33:06 pm 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.43fe4c19e2e46ad718/11/2024, 12:32:30 pm 
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
output: 
[ 
    { 
        "Skype ID": "live:.cid.43fe4c19e2e46ad7", 
        "Timestamp": "2024-11-18 12:34:01", 
        "Message": "ok" 
    }, 
    { 
        "Skype ID": "live:.cid.683c9c4768238bee", 
        "Timestamp": "2024-11-18 12:33:17", 
        "Message": "Message him." 
    }, 
    { 
        "Skype ID": "live:.cid.683c9c4768238bee", 
        "Timestamp": "2024-11-18 12:33:06", 
        "Message": "<contacts><c t=\"s\" s=\"live:pankaj_kumar036_1\" f=\"Pankaj\"></c></contacts>" 
    }, 
    { 
        "Skype ID": "live:.cid.43fe4c19e2e46ad7", 
        "Timestamp": "2024-11-18 12:32:30", 
        "Message": "Hello" 
    } 
]