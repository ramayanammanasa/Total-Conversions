import re 
from datetime import datetime 
def parse_chat_log(chat_log): 
messages = [] 
pattern = re.compile(r'(live:\S+)\s(\d{2}/\d{2}/\d{4}, \d{1,2}:\d{2}:\d{2} (?:am|pm))\n(.*)') 
for match in pattern.finditer(chat_log): 
sender = match.group(1) 
t
 imestamp_str = match.group(2) 
message = match.group(3) 
t
 imestamp = datetime.strptime(timestamp_str, "%d/%m/%Y, %I:%M:%S %p") 
messages.append((timestamp, sender, message)) 
messages.sort()  # Sorting by timestamp 
for timestamp, sender, message in messages: 
print(f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {sender}: {message}") 
chat_log = """live:.cid.e5a0dbcde943f69f11/11/2024, 7:50:48 pm\nyes maam he 
responded\nlive:.cid.683c9c4768238bee11/11/2024, 7:19:19 pm\nHello sima\nDid pankaj sir 
respond to your message or not?\nlive:.cid.e5a0dbcde943f69f11/11/2024, 6:49:22 pm\nok 
maam\nlive:.cid.683c9c4768238bee11/11/2024, 10:15:17 am\nMessage to Pankaj sir at sharp 
7:00pm.\nlive:.cid.683c9c4768238bee11/11/2024, 10:14:28 am\n<contacts><c t="s" 
s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts>\nlive:.cid.683c9c4768238bee11/11/2024, 
10:14:12 am\nYour timing is 7:00pm -9:00pm ryt?\nlive:.cid.683c9c4768238bee11/11/2024, 
10:13:33 am\nHello sima\nlive:.cid.e5a0dbcde943f69f10/11/2024, 5:36:39 pm\n<ss 
type="hi">(wave)</ss>""" 
parse_chat_log(chat_log) 
Copilot 
import base64 
import json 
from urllib.parse import unquote 
# Encoded data from the URIObject 
encoded_data = 
"W3siaWQiOiJ0cmF2ZWwtd2l0aC1haSIsInRpdGxlIjoiTGV0XHUwMDI3cyAjVHJhdmVsV2l0aEFJIiwicHJv
 bXB0IjoiQ2FuIHlvdSBwcmVwYXJlIGFuIGl0aW5lcmFyeSBmb3IgbWUgYW5kIG15IGZyaWVuZHMgdG8g
 dmlzaXQgTG9uZG9uIGZvciA0IGRheXM/IiwiaWNvbiI6InRyYXZlbCIsImNvbG9yIjoiY2F0ZWdvcnkxIn0sey
 JpZCI6Im1hc3Rlci1yZWNpcGVzIiwidGl0bGUiOiJNYXN0ZXIgI0FJQ2hlZiByZWNpcGVzIiwicHJvbXB0IjoiV2
 hhdCBhcmUgc29tZSBvZiB0aGUgbW9zdCB0cmVuZGluZyByZWNpcGVzIHRoZXNlIGRheXM/IiwiaWNvbiI
 6ImNyZWF0ZSIsImNvbG9yIjoiY2F0ZWdvcnkzIn0seyJpZCI6ImJ1c2luZXNzLWdlbml1cyIsInRpdGxlIjoiQm
 UgYW4gI0FJQnVzaW5lc3MgZ2VuaXVzIiwicHJvbXB0IjoiV2hhdCBhcmUgdG9wIGJ1c2luZXNzIGlkZWFzIH
 RoYXQgd2lsbCBncm93IHRoaXMgeWVhcj8gUHJlcGFyZSBhIHBsYW4gZm9yIHRoZW0gYW5kIGdpdmUg
 ZXhwbGFuYXRpb24gd2h5IHlvdSBjaG9zZSB0aGVzZS4iLCJpY29uIjoiZWR1Y2F0aW9uIiwiY29sb3IiOiJjYX
 RlZ29yeTUifV0=" 
# Decode the base64 string 
decoded_bytes = base64.b64decode(encoded_data) 
decoded_str = decoded_bytes.decode('utf-8') 
# Parse JSON data 
decoded_json = json.loads(decoded_str) 
# Pretty print the result 
print(json.dumps(decoded_json, indent=4, ensure_ascii=False))