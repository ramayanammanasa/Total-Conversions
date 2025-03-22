import re 
from datetime import datetime 
# Sample log data 
log_data = """ 
19:6ec4e06893774c9d931d8c3fd5ac18d8@thread.skype4/12/2024, 7:40:00 pm 
<deletemember><eventtime>1733321400999</eventtime><initiator>8:live:.cid.9fa1af1d0ec1257f</i
 nitiator><target>8:live:.cid.9fa1af1d0ec1257f</target></deletemember> 
live:pankaj_kumar036_17/11/2024, 11:13:44 am 
why didnot you send her job description? 
live:pankaj_kumar036_17/11/2024, 11:08:04 am 
Hi <at id="8:live:.cid.9fa1af1d0ec1257f">Jagriti</at> 
19:6ec4e06893774c9d931d8c3fd5ac18d8@thread.skype7/11/2024, 11:07:54 am 
<addmember><eventtime>1730957874169</eventtime><initiator>8:live:pankaj_kumar036_1</initia
 tor><target>8:live:.cid.683c9c4768238bee</target><target>8:live:.cid.9fa1af1d0ec1257f</target></
 addmember> 
19:6ec4e06893774c9d931d8c3fd5ac18d8@thread.skype7/11/2024, 11:07:53 am 
<historydisclosedupdate><eventtime>1730957873716</eventtime><initiator>8:live:pankaj_kumar03
 6_1</initiator><value>true</value></historydisclosedupdate> 
19:6ec4e06893774c9d931d8c3fd5ac18d8@thread.skype7/11/2024, 11:07:53 am 
<joiningenabledupdate><eventtime>1730957873200</eventtime><initiator>8:live:pankaj_kumar036
 _1</initiator><value>true</value></joiningenabledupdate> 
19:6ec4e06893774c9d931d8c3fd5ac18d8@thread.skype7/11/2024, 11:07:52 am 
<addmember><eventtime>1730957872935</eventtime><initiator>8:live:pankaj_kumar036_1</initia
 tor><target>8:live:pankaj_kumar036_1</target></addmember> 
19:6ec4e06893774c9d931d8c3fd5ac18d8@thread.skype7/11/2024, 11:07:52 am 
<historydisclosedupdate><eventtime>1730957872935</eventtime><initiator>8:live:pankaj_kumar03
 6_1</initiator><value>false</value></historydisclosedupdate> 
""" 
# Regular expression to extract timestamped messages 
message_pattern = re.compile(r"(live:[\w._-]+|\d+:[\w@.-]+)\/(\d{1,2}\/\d{1,2}\/\d{4}), 
(\d{1,2}:\d{2}:\d{2} (?:am|pm))\n(.+)", re.DOTALL) 
# Regular expression to extract XML-like events 
event_pattern = 
re.compile(r"<(\w+)><eventtime>(\d+)</eventtime><initiator>([^<]+)</initiator>(?:<target>([^<]+)</
 target>)?(?:<value>([^<]+)</value>)?</\w+>") 
# Extract and structure data 
messages = [] 
events = [] 
for match in message_pattern.finditer(log_data): 
skype_id, date_str, time_str, message = match.groups() 
datetime_obj = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y, %I:%M:%S %p") 
messages.append({ 
"Skype ID": skype_id, 
"Timestamp": datetime_obj.strftime("%Y-%m-%d %H:%M:%S"), 
"Message": message.strip() 
}) 
for match in event_pattern.finditer(log_data): 
event_type, event_time, initiator, target, value = match.groups() 
event_datetime = datetime.utcfromtimestamp(int(event_time) / 1000).strftime('%Y-%m-%d 
%H:%M:%S') 
events.append({ 
"Event Type": event_type, 
"Timestamp": event_datetime, 
"Initiator": initiator, 
"Target": target if target else None, 
"Value": value if value else None 
}) 
# Print structured data 
print("Messages:") 
for msg in messages: 
print(msg) 
print("\nEvents:") 
for event in events: 
print(event) 
Messages: 
{'Skype ID': 'live:pankaj_kumar036_1', 'Timestamp': '2024-11-17 11:13:44', 'Message': 'why didnot 
you send her job description?'} 
{'Skype ID': 'live:pankaj_kumar036_1', 'Timestamp': '2024-11-17 11:08:04', 'Message': 'Hi Jagriti'} 
Events: 
{'Event Type': 'deletemember', 'Timestamp': '2024-12-04 19:40:00', 'Initiator': 
'8:live:.cid.9fa1af1d0ec1257f', 'Target': '8:live:.cid.9fa1af1d0ec1257f', 'Value': None} 
{'Event Type': 'addmember', 'Timestamp': '2024-11-07 11:07:54', 'Initiator': 
'8:live:pankaj_kumar036_1', 'Target': '8:live:.cid.683c9c4768238bee', 'Value': None} 
{'Event Type': 'historydisclosedupdate', 'Timestamp': '2024-11-07 11:07:53', 'Initiator': 
'8:live:pankaj_kumar036_1', 'Target': None, 'Value': 'true'} 