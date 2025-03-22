import re 
from datetime import datetime 
# Sample log data 
log_data = """ 
live:.cid.adb9bef74b0fda4515/12/2024, 7:43:32 pm 
okay 
live:.cid.683c9c4768238bee15/12/2024, 7:00:58 pm 
Message him tomorrow 
live:.cid.683c9c4768238bee15/12/2024, 7:00:25 pm 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.adb9bef74b0fda4515/12/2024, 5:50:00 pm 
hi 
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