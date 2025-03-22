import re 
import json 
from datetime import datetime 
# Sample chat log data 
chat_log = """ 
live:.cid.aa589a6ff86171e819/11/2024, 11:02:18 am 
Cool. 
live:.cid.683c9c4768238bee19/11/2024, 11:01:57 am 
Yeah 
live:.cid.aa589a6ff86171e819/11/2024, 11:01:34 am 
Will ping him at 11:30. Will that be fine ? 
live:.cid.aa589a6ff86171e819/11/2024, 11:01:10 am 
Okay. 
live:.cid.683c9c4768238bee19/11/2024, 11:00:48 am 
Message him on time. 
live:.cid.683c9c4768238bee19/11/2024, 11:00:27 am 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.683c9c4768238bee19/11/2024, 11:00:18 am 
Hello Divya 
live:.cid.aa589a6ff86171e819/11/2024, 10:58:43 am 
Divya here.. 
live:.cid.aa589a6ff86171e819/11/2024, 10:58:36 am 
Hello Isha. 
live:.cid.aa589a6ff86171e819/11/2024, 10:58:31 am 
<ss type="hi">(wave)</ss> 
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
"Skype ID": "live:.cid.aa589a6ff86171e8", 
        "Timestamp": "2024-11-19 11:02:18", 
        "Message": "Cool." 
    }, 
    { 
        "Skype ID": "live:.cid.683c9c4768238bee", 
        "Timestamp": "2024-11-19 11:01:57", 
        "Message": "Yeah" 
    }, 
    { 
        "Skype ID": "live:.cid.aa589a6ff86171e8", 
        "Timestamp": "2024-11-19 11:01:34", 
        "Message": "Will ping him at 11:30. Will that be fine?" 
    }, 
    { 
        "Skype ID": "live:.cid.aa589a6ff86171e8", 
        "Timestamp": "2024-11-19 11:01:10", 
        "Message": "Okay." 
    }, 
    { 
        "Skype ID": "live:.cid.683c9c4768238bee", 
        "Timestamp": "2024-11-19 11:00:48", 
        "Message": "Message him on time." 
    }, 
    { 
        "Skype ID": "live:.cid.683c9c4768238bee", 
        "Timestamp": "2024-11-19 11:00:27", 
        "Message": "<contacts><c t=\"s\" s=\"live:pankaj_kumar036_1\" f=\"Pankaj\"></c></contacts>" 
    }, 
    { 
        "Skype ID": "live:.cid.683c9c4768238bee", 
        "Timestamp": "2024-11-19 11:00:18", 
        "Message": "Hello Divya" 
    }, 
    { 
        "Skype ID": "live:.cid.aa589a6ff86171e8", 
        "Timestamp": "2024-11-19 10:58:43", 
        "Message": "Divya here.." 
    }, 
    { 
        "Skype ID": "live:.cid.aa589a6ff86171e8", 
        "Timestamp": "2024-11-19 10:58:36", 
        "Message": "Hello Isha." 
    }, 
    { 
        "Skype ID": "live:.cid.aa589a6ff86171e8", 
        "Timestamp": "2024-11-19 10:58:31", 
        "Message": "<ss type=\"hi\">(wave)</ss>" 
    } 
]