import re 
import json 
chat_data = """ 
live:.cid.683c9c4768238bee6/12/2024, 9:56:37 pm 
Hello <at id="8:live:.cid.d5ad247b07f4e839">Aprajita</at> 
live:.cid.683c9c4768238bee6/12/2024, 5:29:30 pm 
This document contains a step to step process of taking interviews of candidates. You need to ask the 
upper 7 questions only to ignore the one below. Must check it and ask me if you have any questions . 
live:.cid.683c9c4768238bee6/12/2024, 5:28:01 pm 
<URIObject uri="https://api.asm.skype.com/v1/objects/0-jhb-d7
80e36f8f550a68f01f5598b627d09016" url_thumbnail="https://api.asm.skype.com/v1/objects/0-jhb
d7-80e36f8f550a68f01f5598b627d09016/views/original" type="File.1/Word.1" doc_id="0-jhb-d7
80e36f8f550a68f01f5598b627d09016">To view this file, go to: <a 
href="https://login.skype.com/login/sso?go=webclient.xmm&docid=0-jhb-d7
80e36f8f550a68f01f5598b627d09016">https://login.skype.com/login/sso?go=webclient.xmm&doci
 d=0-jhb-d7-80e36f8f550a68f01f5598b627d09016</a><OriginalName v="Telephonic interview 
process for hr intern (1) (1).docx"></OriginalName><FileSize v="15486"></FileSize></URIObject> 
live:.cid.d5ad247b07f4e8396/12/2024, 12:40:33 pm 
done 
live:.cid.683c9c4768238bee6/12/2024, 12:39:11 pm 
Msg him. 
live:.cid.683c9c4768238bee6/12/2024, 12:38:48 pm 
<contacts><c t="s" s="live:pankaj_kumar036_1" f="Pankaj"></c></contacts> 
live:.cid.683c9c4768238bee6/12/2024, 12:38:40 pm 
Hello 
live:.cid.d5ad247b07f4e8396/12/2024, 12:36:56 pm 
<ss type="hi">(wave)</ss> 
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
# Convert to JSON for readability 
json_output = json.dumps(structured_data, indent=4) 
print(json_output)