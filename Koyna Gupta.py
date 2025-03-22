import re 
from datetime import datetime 
 
def parse_chat_log(chat_log): 
    parsed_messages = [] 
     
    message_pattern = re.compile(r'live:\.cid\.[\w]+/(\d+/\d+/\d+, \d+:\d+:\d+ [ap]m)\\n(.*?)$', 
re.MULTILINE) 
    link_pattern = re.compile(r'https?://\S+') 
     
    for match in message_pattern.finditer(chat_log): 
        timestamp_str, message = match.groups() 
        try: 
            timestamp = datetime.strptime(timestamp_str, "%m/%d/%Y, %I:%M:%S %p") 
        except ValueError: 
            timestamp = timestamp_str  # Keep as string if format doesn't match 
         
        links = link_pattern.findall(message) 
        parsed_messages.append({ 
            "timestamp": timestamp, 
            "message": message.strip(), 
            "links": links 
        }) 
     
    return parsed_messages 
 
def main(): 
    chat_log = """(Paste your chat log text here)""" 
    parsed_data = parse_chat_log(chat_log) 
     
    for entry in parsed_data: 
        print(f"Time: {entry['timestamp']}") 
        print(f"Message: {entry['message']}") 
        if entry['links']: 
            print(f"Links: {', '.join(entry['links'])}") 
        print("-" * 40) 
 
if _name_ == "_main_": 
    main() 
Eva Jain 
import re 
 
chat_log = """PASTE YOUR CHAT LOG HERE""" 
 
def extract_data(chat_log): 
    pattern = re.compile(r'(?P<id>live:\.cid\.[\w]+)(?P<timestamp>\d{2}/\d{2}/\d{4}, 
\d{1,2}:\d{2}:\d{2} [ap]m)\n(?P<message>.*?)\n', re.DOTALL) 
    media_pattern = re.compile(r'(?P<media_url>https://api\.asm\.skype\.com/v1/objects/[\w-]+)') 
    link_pattern = re.compile(r'(?P<link>https?://[\w./?=-]+)') 
     
    extracted_data = [] 
     
    for match in pattern.finditer(chat_log): 
        entry = { 
            "User ID": match.group('id'), 
            "Timestamp": match.group('timestamp'), 
            "Message": match.group('message').strip(), 
            "Media Links": media_pattern.findall(match.group('message')), 
            "Other Links": link_pattern.findall(match.group('message')) 
        } 
        extracted_data.append(entry) 
     
    return extracted_data 
 
chat_data = extract_data(chat_log) 
 
for entry in chat_data: 
    print(entry) 
