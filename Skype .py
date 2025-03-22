import json 
from datetime import datetime 
 
# Sample Skype engagement message 
skype_message = """ 
[{ 
    "contentType": "application/vnd.microsoft.card.popup", 
    "cardType": 1, 
    "quietCard": false, 
    "iconUrl": 
"https://az705183.vo.msecnd.net/dam/skype/media/engagement/skypeengagementsystem
test/6494736c-6abf-41a9-a62f-785857952e06_nps%20card-3%20icon.jpg", 
    "campaignGuid": "nps-mobile-v6-c-new", 
    "language": "en-gb", 
    "platformList": [1, 2, 1445], 
    "validUntilTimestamp": "2025-02-05T12:27:31.9013417Z", 
    "content": { 
        "actionUri": 
"https://feedback.skype.com/survey/answer/nps?utm_source=engagementcard&lang=en-gb", 
        "actionTarget": "feedbackBrowser", 
        "title": "Help improve Skype", 
        "text": "Shape the future of Skype by telling us what you think of the app.", 
        "media": { 
            "url": 
"https://az705183.vo.msecnd.net/dam/skype/media/engagement/skypeengagementsystem
test/980796cb-c8ca-4e77-b562-a38f77865153_nps%20card-3.2.jpg", 
            "mediaType": "image" 
        }, 
        "buttons": [{ 
            "actionUri": 
"https://feedback.skype.com/survey/answer/nps?utm_source=engagementcard&lang=en-gb", 
            "title": "OK, yes", 
            "actionTarget": "feedbackBrowser" 
        }] 
    }, 
    "telemetry": { 
        "campaignId": "nps-mobile", 
        "variantId": "nps-mobile-c", 
        "iteration": "1" 
    }, 
    "experimentName": "nps-mobile" 
}] 
""" 
 
# Parse JSON data 
data = json.loads(skype_message) 
 
# Extract relevant details 
for item in data: 
    valid_until = datetime.fromisoformat(item["validUntilTimestamp"].replace("Z", "")) 
    print(f"Title: {item['content']['title']}") 
    print(f"Message: {item['content']['text']}") 
    print(f"Survey Link: {item['content']['actionUri']}") 
    print(f"Image URL: {item['content']['media']['url']}") 
    print(f"Valid Until: {valid_until}") 
    print(f"Experiment Name: {item['experimentName']}")