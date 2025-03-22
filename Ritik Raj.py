import re 
import json 
from datetime import datetime 
 
# Sample chat log data 
chat_log = """ 
live:.cid.683c9c4768238bee14/11/2024, 10:06:52 pm 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.b001863881d84ef114/11/2024, 9:02:28 pm 
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