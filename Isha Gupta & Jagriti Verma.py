import re 
import json 
# Raw chat log data 
chat_log = """ 
# (Paste the chat log here) 
""" 
# Regular expressions to capture different patterns 
message_pattern = re.compile(r'live:[\w.]+ (\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{1,2}:\d{2} 
(?:am|pm))\n(.+)') 
event_pattern = re.compile(r'<(\w+)>(.*?)</\1>') 
quote_pattern = re.compile(r'<quote 
author="(.+?)".*?>(.*?)<legacyquote>.*?</legacyquote></quote>', re.DOTALL) 
# Parsing messages 
messages = [] 
for match in message_pattern.finditer(chat_log): 
t
 imestamp, message = match.groups() 
messages.append({"timestamp": timestamp, "message": message}) 
# Parsing special events (e.g., member added/removed, updates) 
events = [] 
for match in event_pattern.finditer(chat_log): 
event_type, details = match.groups() 
events.append({"event": event_type, "details": details.strip()}) 
# Parsing quoted messages 
quotes = [] 
for match in quote_pattern.finditer(chat_log): 
author, content = match.groups() 
quotes.append({"author": author, "content": content.strip()}) 
# Output structured data 
parsed_data = { 
"messages": messages, 
"events": events, 
"quotes": quotes 
} 
# Print parsed data as JSON 
print(json.dumps(parsed_data, indent=4)) 