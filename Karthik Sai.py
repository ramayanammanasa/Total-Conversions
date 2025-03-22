import re 
from datetime import datetime 
# Sample messages 
messages = [ 
("live:.cid.683c9c4768238bee", "4/12/2024, 9:24:23 pm", "Okayy"), 
("live:.cid.cb8f121cdf809563", "4/12/2024, 9:01:14 pm", "She told me after the exams I'll talk to 
you"), 
("live:.cid.683c9c4768238bee", "4/12/2024, 9:00:45 pm", "Okay"), 
("live:.cid.cb8f121cdf809563", "4/12/2024, 9:00:34 pm", "She told me she wants to join after the 
exams, it means Feb month 2025 ...work time not told"), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:59:39 pm", "Joining date?"), 
("live:.cid.cb8f121cdf809563", "4/12/2024, 8:57:50 pm", """HR INTERNSHIP 
Name- Divya Sharma 
Email ID - divyasharma200707@gmail.com 
Joining date - 
Duration -2 months 
Contact no -9440472843 
Working time - 
Address -"""), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:55:06 pm", "Ok"), 
("live:.cid.cb8f121cdf809563", "4/12/2024, 8:53:47 pm", "Ok wait"), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:42:01 pm", "And now ask me to take his/her details 
from you."), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:41:36 pm", "Pankaj sir told me someone is 
interested and you contacted him/her"), 
("live:.cid.cb8f121cdf809563", "4/12/2024, 8:40:13 pm", "Which candidates?"), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:35:47 pm", """HR INTERNSHIP 
Name- 
Email ID - 
Joining date - 
Duration - 
Contact no - 
Working time - 
Address -"""), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:35:28 pm", "Please share the details of new 
candidates in the format."), 
("live:.cid.683c9c4768238bee", "4/12/2024, 8:35:01 pm", "Hello Karthik"), 
] 
 
# Function to parse date 
def parse_date(date_str): 
    return datetime.strptime(date_str, "%d/%m/%Y, %I:%M:%S %p") 
 
# Extract HR internship details 
hr_details = {} 
for sender, timestamp, message in messages: 
    date_obj = parse_date(timestamp) 
     
    if "HR INTERNSHIP" in message: 
        name_match = re.search(r"Name-\s*(.*)", message) 
        email_match = re.search(r"Email ID -\s*([\w\.\-]+@[\w\.\-]+)", message) 
        duration_match = re.search(r"Duration -\s*(.*)", message) 
        contact_match = re.search(r"Contact no -\s*(\d+)", message) 
         
        hr_details = { 
            "name": name_match.group(1) if name_match else "Not provided", 
            "email": email_match.group(1) if email_match else "Not provided", 
            "duration": duration_match.group(1) if duration_match else "Not provided", 
            "contact": contact_match.group(1) if contact_match else "Not provided", 
        } 
 
# Display extracted HR details 
print("Extracted HR Internship Details:") 
print(hr_details) 
 
# Display all messages in structured format 
print("\nFormatted Messages:") 
for msg in messages: 
print(f"[{parse_date(msg[1])}] {msg[0]}: {msg[2]}")