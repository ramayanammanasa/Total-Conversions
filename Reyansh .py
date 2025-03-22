import re 
import datetime 
# Sample chat log 
chat_log = """ 
live:.cid.683c9c4768238bee2/12/2024, 8:48:48 pm 
If you have any issues or work on your sheet then you can do that. 
live:.cid.538e18075e03f2b72/12/2024, 8:48:48 pm 
Ok 
live:.cid.683c9c4768238bee2/12/2024, 8:48:26 pm 
No I'm not working. I already told him that it's not possible for me to work on so many sheets today. 
So I will work on your sheet tomorrow morning. 
live:.cid.538e18075e03f2b72/12/2024, 8:46:56 pm 
Ok work on what you are working on. After that continue from tomorrow onwards 
live:.cid.538e18075e03f2b72/12/2024, 8:46:19 pm 
But sir told you are working on that. 
live:.cid.683c9c4768238bee2/12/2024, 8:35:44 pm 
No actually I have lots of work today so that I'm unable to work on your sheet 
""" 
# Regular expression to match Skype ID, timestamp, and message 
pattern = re.compile(r"(live:.cid.[a-fA-F0-9]+)\/(\d{1,2}\/\d{4}), (\d{1,2}:\d{2}:\d{2} 
[apAP][mM])\n(.+)", re.MULTILINE) 
# Extract messages into a structured format 
messages = [] 
for match in pattern.finditer(chat_log): 
skype_id, date, time, message = match.groups() 
t
 imestamp = datetime.datetime.strptime(f"{date} {time}", "%m/%Y %I:%M:%S %p")  # Convert to 
datetime object 
messages.append({"Skype ID": skype_id, "Timestamp": timestamp, "Message": message.strip()}) 
# Print structured data 
for msg in messages: 
print(msg) 