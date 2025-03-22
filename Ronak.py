import re 
from datetime import datetime 
log_text = """ 
live:.cid.454ab343a5e9e2e925/11/2024, 8:07:51 pm  
i already<e_m a="live:.cid.454ab343a5e9e2e9" ts_ms="1732545471822" ts="1732545471" 
t="61"></e_m> 
live:.cid.454ab343a5e9e2e923/1/2025, 10:05:05 pm 
i already<e_m a="live:.cid.454ab343a5e9e2e9" ts_ms="1732545471822" ts="1732545471" 
t="61"></e_m> 
live:.cid.454ab343a5e9e2e916/12/2024, 8:02:01 pm 
Also i my exams are starting from tomorrow itself so i'll not be available further.... 
live:.cid.454ab343a5e9e2e916/12/2024, 7:59:45 pm 
I would like to inform you that my internship period is over for the 1month and now i don't want to 
continue further . So, i request you to please provide me the internship letter etc.... 
""" 
pattern = re.compile(r'live:(\S+)/(\d{1,2}/\d{4}), (\d{1,2}:\d{2}:\d{2} [ap]m)\n(.*?)(?=\nlive:|\Z)', 
re.DOTALL) 
messages = [] 
for match in pattern.finditer(log_text): 
user_id, date, time, message = match.groups() 
t
 imestamp = datetime.strptime(f"{date} {time}", "%m/%Y, %I:%M:%S %p") 
messages.append({ 
"User ID": user_id, 
"Timestamp": timestamp, 
"Message": message.strip() 
}) 
for msg in messages: 
print(f"[{msg['Timestamp']}] User {msg['User ID']} said: {msg['Message']}\n")