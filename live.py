import re 
from datetime import datetime 
# Sample log data 
log_data = "live:.cid.1b156b7f6720c37710/12/2024, 4:05:52 pm\nHii Mam This Venu" 
# Regular expression to extract Skype ID, date, time, and message 
pattern = r"(live:[\w.]+)\/(\d{1,2}\/\d{1,2}\/\d{4}), (\d{1,2}:\d{2}:\d{2} (?:am|pm))\n(.*)" 
# Extract details using regex 
match = re.match(pattern, log_data, re.DOTALL) 
if match: 
skype_id, date_str, time_str, message = match.groups() 
# Convert date and time to a standard format 
datetime_str = f"{date_str} {time_str}" 
datetime_obj = datetime.strptime(datetime_str, "%d/%m/%Y, %I:%M:%S %p") 
# Create structured data 
decoded_message = { 
"Skype ID": skype_id, 
"Timestamp": datetime_obj.strftime("%Y-%m-%d %H:%M:%S"), 
"Message": message.strip() 
} 
# Print structured output 
print(decoded_message) 
else: 
print("No match found.") 
{ 
} 
"Skype ID": "live:.cid.1b156b7f6720c377", 
"Timestamp": "2024-12-10 16:05:52", 
"Message": "Hii Mam This Venu" 