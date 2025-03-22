import re 
 
def parse_call_logs(log_data): 
    call_logs = [] 
    pattern = re.compile(r'live:\.cid\.(\w+)/(\d{1,2}/\d{1,2}/\d{4}), (\d{1,2}:\d{2}:\d{2} [ap]m)\nCall 
Logs for Call (\w{8}-\w{4}-\w{4}-\w{4}-\w{12})') 
     
    matches = pattern.findall(log_data) 
     
    for match in matches: 
        call_logs.append({ 
            "caller_id": match[0], 
            "date": match[1], 
            "time": match[2], 
            "call_id": match[3] 
        }) 
     
    return call_logs 
 
# Example log data 
log_data = """live:.cid.683c9c4768238bee29/12/2024, 7:32:23 pm 
Call Logs for Call bf33a6ce-a731-409b-9e1f-150664dde9b5 
live:.cid.683c9c4768238bee24/12/2024, 11:52:02 am 
Call Logs for Call a6ecdc96-d202-4fb3-b3ac-82b340677a08""" 
 
parsed_logs = parse_call_logs(log_data) 
 
for log in parsed_logs: 
    print(log)