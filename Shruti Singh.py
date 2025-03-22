import re 
 
def parse_chat_log(chat_log): 
    pattern = re.compile(r"live:(\.cid\.[0-9a-f]+)/(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}:\d{2} 
(?:am|pm))\n(.*?)$", re.MULTILINE) 
     
    parsed_data = [] 
    for match in pattern.finditer(chat_log): 
        user_id, date, time, message = match.groups() 
        parsed_data.append({ 
            "user_id": user_id, 
            "date": date, 
            "time": time, 
            "message": message.strip() 
        }) 
     
    return parsed_data 
 
# Example usage: 
chat_log = """PASTE YOUR CHAT LOG HERE""" 
parsed_chat = parse_chat_log(chat_log) 
 
for entry in parsed_chat: 
print(f"[{entry['date']} {entry['time']}] {entry['user_id']}: {entry['message']}") 
live:pankaj_kumar036_1, live:.cid.683c9c4768238bee, ... 
import re 
from datetime import datetime 
def parse_chat_log(chat_log): 
messages = [] 
pattern = re.compile(r"(live:[^\s]+)/(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}:\d{2} (?:am|pm))\n(.*)", 
re.MULTILINE) 
for match in pattern.finditer(chat_log): 
user, date, time, message = match.groups() 
t
 imestamp = datetime.strptime(f"{date} {time}", "%d/%m/%Y %I:%M:%S %p") 
messages.append({"user": user, "timestamp": timestamp, "message": message}) 
return messages 
def display_messages(messages): 
for msg in sorted(messages, key=lambda x: x["timestamp"]): 
print(f"[{msg['timestamp']}] {msg['user']}: {msg['message']}") 
chat_log = """ 
live:.cid.9b8105e4e63fca9714/11/2024, 7:15:25 pm 
<partlist type="ended" alt=""><part 
identity="live:pankaj_kumar036_1"><name>live:pankaj_kumar036_1</name><duration>1382</dur
 ation></part><part 
identity="live:.cid.9b8105e4e63fca97"><name>live:.cid.9b8105e4e63fca97</name><duration>1382
 </duration></part><part 
identity="live:.cid.683c9c4768238bee"><name>live:.cid.683c9c4768238bee</name><duration>1382
 </duration></part></partlist> 
live:pankaj_kumar036_114/11/2024, 7:11:20 pm 
I am trying to post a job but is showing you reached the limit 
I would to know when I can post next job? 
live:pankaj_kumar036_114/11/2024, 6:59:58 pm 
Consumer Insurance Specialist 
live:pankaj_kumar036_114/11/2024, 6:57:16 pm 
<partlist type="started" alt=""><part 
identity="live:pankaj_kumar036_1"><name>live:pankaj_kumar036_1</name></part></partlist> 
""" 
parsed_messages = parse_chat_log(chat_log) 
display_messages(parsed_messages) 
Prateek 
import re 
def parse_chat_logs(logs): 
messages = [] 
pattern = re.compile(r'live:\S+\s(\d{2}/\d{2}/\d{4},\s\d{1,2}:\d{2}:\d{2}\s(?:am|pm))\n(.*)') 
for match in pattern.finditer(logs): 
t
 imestamp, message = match.groups() 
messages.append((timestamp, message)) 
messages.sort() 
for timestamp, message in messages: 
print(f'[{timestamp}] {message}') 
chat_logs = """ 
live:.cid.5f2e9b2a25440e2112/11/2024, 11:37:29 am 
<quote author="live:.cid.683c9c4768238bee" authorname="Isha Gupta" timestamp="1731388989" 
conversation="8:live:.cid.683c9c4768238bee" messageid="1731388988805" 
cuid="15239475056701259543"><legacyquote>[1731388989] Isha Gupta: </legacyquote>Message 
to sir at sharp 5:00pm<legacyquote> 
<<< </legacyquote></quote>Ohk 
live:.cid.683c9c4768238bee12/11/2024, 10:53:07 am 
Message to sir at sharp 5:00pm 
live:.cid.683c9c4768238bee12/11/2024, 10:52:24 am 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.683c9c4768238bee12/11/2024, 10:51:59 am 
Hello Prateek 
live:.cid.5f2e9b2a25440e2111/11/2024, 10:42:53 pm 
Prateek this side 
live:.cid.5f2e9b2a25440e2111/11/2024, 10:42:42 pm
<ss type="hi">(wave)</ss> 
""" 
parse_chat_logs(chat_logs)