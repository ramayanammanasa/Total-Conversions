import re 
from datetime import datetime 
# Sample Skype chat messages 
messages = [ 
("live:.cid.683c9c4768238bee", "12/12/2024, 10:29:32 am", "Okay great!"), 
("live:.cid.55b5302b4fd5cafc", "11/12/2024, 10:46:17 pm", "Added the leads on the sheet"), 
("live:.cid.55b5302b4fd5cafc", "11/12/2024, 10:19:38 pm", "I got the access"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 10:17:29 pm", "You did a message to him or received 
a message from him?"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 10:05:02 pm", "If right now you are not available... 
send it to Deeksha ma'am."), 
("live:.cid.55b5302b4fd5cafc", "11/12/2024, 10:06:08 pm", "For this, I have messaged Pankaj sir"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 9:55:59 pm", "Please update your LinkedIn job post 
lead"), 
("live:.cid.683c9c4768238bee", "11/12/2024, 9:56:01 pm", 
"https://docs.google.com/spreadsheets/d/1Pq2Q-Kup8vOsXwE3xIFjz
GN4ayymBg1bU4O31b6e9k/edit?usp=sharing"), 
("live:.cid.55b5302b4fd5cafc", "10/12/2024, 6:44:39 pm", "I have logged in"), 
("live:.cid.55b5302b4fd5cafc", "10/12/2024, 6:44:26 pm", "(wave)") 
] 
# Function to parse date 
def parse_date(date_str): 
return datetime.strptime(date_str, "%d/%m/%Y, %I:%M:%S %p") 
# Extract Google Sheets links 
sheet_links = [] 
linkedin_instructions = [] 
structured_messages = [] 
for sender, timestamp, message in messages: 
date_obj = parse_date(timestamp) 
# Detect Google Sheets links 
sheet_match = re.search(r"https://docs\.google\.com/spreadsheets/[\w\d\-_/]+", message) 
if sheet_match: 
sheet_links.append(sheet_match.group()) 
# Detect LinkedIn instructions 
if "LinkedIn" in message or "job post" in message or "view applicants" in message: 
linkedin_instructions.append(message) 
# Store structured messages 
structured_messages.append((date_obj, sender, message)) 
# Sorting messages chronologically 
structured_messages.sort() 
# Print structured chat logs 
print("\n--- Formatted Chat Logs ---") 
for msg in structured_messages: 
print(f"[{msg[0]}] {msg[1]}: {msg[2]}") 
# Print extracted Google Sheets links 
print("\n--- Extracted Google Sheets Links ---") 
for link in sheet_links: 
print(link) 
# Print LinkedIn-related instructions 
print("\n--- LinkedIn Instructions ---") 
for instruction in linkedin_instructions: 
print(instruction)