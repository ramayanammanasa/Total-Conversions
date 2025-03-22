import re 
import json 
# Sample chat data 
chat_data = """ 
live:.cid.683c9c4768238bee6/12/2024, 5:29:50 pm 
This document contains a step to step process of taking interviews of candidates. You need to ask the 
upper 7 questions only to ignore the one below. Must check it and ask me if you have any questions . 
live:.cid.683c9c4768238bee6/12/2024, 5:29:41 pm 
<URIObject uri="https://api.asm.skype.com/v1/objects/0-jhb-d7
c69b619b2996225e539c9322fd89fb04" url_thumbnail="https://api.asm.skype.com/v1/objects/0
jhb-d7-c69b619b2996225e539c9322fd89fb04/views/original" type="File.1" doc_id="0-jhb-d7
c69b619b2996225e539c9322fd89fb04">To view this file, go to: <a 
href="https://login.skype.com/login/sso?go=webclient.xmm&docid=0-jhb-d7
c69b619b2996225e539c9322fd89fb04">https://login.skype.com/login/sso?go=webclient.xmm&doci
 d=0-jhb-d7-c69b619b2996225e539c9322fd89fb04</a><OriginalName v="Telephonic interview 
process for hr intern (1) (1).docx"></OriginalName><FileSize v="15486"></FileSize></URIObject> 
live:.cid.683c9c4768238bee6/12/2024, 12:37:34 pm 
Okay 
live:.cid.2a284a1cecc5c6a06/12/2024, 12:37:12 pm 
ND he replied also 
live:.cid.2a284a1cecc5c6a06/12/2024, 12:36:49 pm 
Yess 
live:.cid.683c9c4768238bee6/12/2024, 12:34:09 pm 
Have you messaged him? 
live:.cid.2a284a1cecc5c6a06/12/2024, 12:28:28 pm 
Okk 
live:.cid.683c9c4768238bee6/12/2024, 12:28:18 pm 
Message him rn. 
live:.cid.683c9c4768238bee6/12/2024, 12:28:05 pm 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.2a284a1cecc5c6a06/12/2024, 12:27:51 pm 
<ss type="hi">(wave)</ss> 
""" 
# Regular expression pattern to extract structured data 
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
# Convert to JSON format for readability 
json_output = json.dumps(structured_data, indent=4) 
# Print the structured JSON output 
print(json_output)