import re 
 
chat_data = """ 
live:.cid.13eb190869e0e45d9/12/2024, 10:45:01 am 
ok 
live:.cid.683c9c4768238bee9/12/2024, 10:43:51 am 
Message him according to your time. 
live:.cid.683c9c4768238bee9/12/2024, 10:43:33 am 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.683c9c4768238bee9/12/2024, 10:43:23 am 
Okay 
live:.cid.13eb190869e0e45d9/12/2024, 10:42:41 am 
This is my official ID live:.cid.13eb190869e0e45d 
live:.cid.13eb190869e0e45d9/12/2024, 10:40:57 am 
live:.cid.13eb190869e0e45d Sakshi Patil 
live:.cid.13eb190869e0e45d9/12/2024, 10:40:48 am 
Hii decode the above matter in python code 
""" 
pattern = r"live:(\.cid\.[a-zA-Z0-9]+)\/(\d{1,2}\/\d{4}), (\d{1,2}:\d{2}:\d{2} (?:am|pm))\n(.*?)\n" 
matches = re.findall(pattern, chat_data) 
structured_data = [] 
for match in matches: 
user_id, date, time, message = match 
structured_data.append({ 
"User ID": user_id, 
"Date": date, 
"Time": time, 
"Message": message 
}) 
for entry in structured_data: 
print(entry) 