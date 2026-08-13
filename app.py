import requests
from flask import Flask,request
import os
channel_access_token = os.environ.get('channel_access_token')
def send_text(rp_token,mes):
    json_data = {
        'replyToken': rp_token,
        'messages': [mes],
    }
    print(rp_token)
    response = requests.post('https://api.line.me/v2/bot/message/reply', headers=headers, json=json_data)
    print(response.text)

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {channel_access_token}',
}
app = Flask("Alan")
@app.route("/",methods = ["POST"])
def linebot():
    data = request.get_json()
    if len(data["events"]) == 0:
        print("這是LINE驗證")
    else:
        print(data["events"])
        text = data["events"][0]["message"]["text"]
        rp_token = data["events"][0]["replyToken"]
        print(rp_token)
        mes = {
            "type": "text",
            "text": "串接成功",
            "quickReply": {
  "items": [{
      "type": "action",
      "action":
      {
  "type": "message",
  "label": "Yes",
  "text": "確認"
}},
    {
      "type": "action",
      "action": {
        "type": "cameraRoll",
        "label": "Send photo"
      }
    },
    {
      "type": "action",
      "action": {
        "type": "camera",
        "label": "Open camera"
      }
    }
  ]
}

        }
        send_text(rp_token,mes)
    return "OK",200
if __name__ == "__main__":
    app.run()
