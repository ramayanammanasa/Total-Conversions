import re 
from datetime import datetime 
# Input string 
input_string = "live:.cid.683c9c4768238bee2/12/2024, 9:30:42 pm" 
# Extract Skype ID using regex 
skype_id_match = re.search(r"live:\.cid\.([a-fA-F0-9]+)", input_string) 
skype_id = skype_id_match.group(1) if skype_id_match else "Not found" 
# Extract timestamp 
t
 imestamp_match = re.search(r"(\d{1,2}/\d{1,2}/\d{4}), (\d{1,2}:\d{2}:\d{2} [apAP][mM])", 
input_string) 
if timestamp_match: 
date_str, time_str = timestamp_match.groups() 
t
 imestamp = datetime.strptime(f"{date_str} {time_str}", "%m/%d/%Y %I:%M:%S %p") 
else: 
t
 imestamp = "Not found" 
# Print extracted details 
print("Extracted Skype ID:", skype_id) 
print("Parsed Timestamp:", timestamp)