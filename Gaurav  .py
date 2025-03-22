import re 
from datetime import datetime 
# Sample log data 
log_data = """ 
live:.cid.dc2a7090f3b9683713/12/2024, 8:51:34 pm 
Hey isha if you can short out my completion certificate that would be great 
live:.cid.dc2a7090f3b9683713/12/2024, 6:30:13 pm 
Yeah thank you 
live:.cid.683c9c4768238bee13/12/2024, 6:28:03 pm 
Yes actually he told me about this, but I have some urgent work that's why I'm unable. Once he 
confirms me, I will send you your completion certificate and congratulations also    
live:.cid.dc2a7090f3b9683713/12/2024, 6:26:47 pm 
Sure I will be waiting as pankaj sir was telling that the Certificate will be ready by 10am that why I 
thought to enquire on this 
""" 
# Regular expression to match Skype ID, date, time, and message 
pattern = r"(live:[\w.]+)\/(\d{1,2}\/\d{1,2}\/\d{4}), (\d{1,2}:\d{2}:\d{2} 
(?:am|pm))\n(.*?)(?=\nlive:|$)" 
# Extract and parse messages 
messages = [] 
for match in re.finditer(pattern, log_data, re.DOTALL): 
skype_id, date_str, time_str, message = match.groups() 
# Convert date and time to a standard format 
datetime_str = f"{date_str} {time_str}" 
datetime_obj = datetime.strptime(datetime_str, "%d/%m/%Y, %I:%M:%S %p") 
messages.append({ 
"Skype ID": skype_id, 
"Timestamp": datetime_obj.strftime("%Y-%m-%d %H:%M:%S"), 
"Message": message.strip() 
}) 
# Print structured data 
for msg in messages: 
print(msg)