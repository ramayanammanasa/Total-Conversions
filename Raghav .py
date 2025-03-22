import re 
 
def parse_chat(chat): 
    messages = chat.strip().split("\n") 
    parsed_data = [] 
    contact_list = [] 
     
    contact_pattern = re.compile(r"<contacts><c t=\"s\" s=\"(.*?)\" f=\"(.*?)\"></c></contacts>") 
     
    for message in messages: 
        parts = message.split(", ", 1) 
        if len(parts) == 2: 
            user_info, content = parts 
            contact_match = contact_pattern.search(content) 
            if contact_match: 
                contact_list.append({"ID": contact_match.group(1), "Name": contact_match.group(2)}) 
                continue 
             
            parsed_data.append({ 
                "User": user_info.split("/")[0], 
                "Date": user_info.split("/")[1], 
                "Time": user_info.split(", ")[1], 
                "Message": content 
            }) 
     
    return parsed_data, contact_list 
 
# Sample chat data 
chat_data = """live:.cid.683c9c4768238bee9/12/2024, 11:14:43 am\nMessage him on your joining 
date.\nlive:.cid.fae5979a211d08ff9/12/2024, 11:13:58 am\nDo I have to message him before the 
joining date, or exactly on 16th?\nlive:.cid.683c9c4768238bee9/12/2024, 11:13:13 am\nMessage 
him according to your time\nlive:.cid.683c9c4768238bee9/12/2024, 11:12:01 am\n<contacts><c 
t=\"s\" s=\"live:pankaj_kumar036_1\" 
f=\"Pankaj\"></c></contacts>\nlive:.cid.fae5979a211d08ff9/12/2024, 11:10:13 am\nRaghav 
Khanduja\nlive:.cid.fae5979a211d08ff9/12/2024, 11:09:55 am\nHii""" 
 
parsed_messages, contacts = parse_chat(chat_data) 
 
print("Messages:") 
for msg in parsed_messages: 
    print(msg) 
 
print("\nContacts:") 
for contact in contacts: 
    print(contact)