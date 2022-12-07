import requests
import json
import os

key = os.environ.get('FIREBASE_TOKEN',
                     'AAAAcugoG78:APA91bE5i3yWmaxsZlo8UFsktjBFF9BQVjow0uce0N8jBWCLwVzFZZK-PB4iX44CM5VW2b3g4tfF0mcpExlAiGMfj2BkbUGG0cAelF8x_CHE4kvTAylMfCW6_j15l3OiijEOsdLx-ERL')


class FireBaseRequest:
    url = 'https://fcm.googleapis.com/fcm/send'

    def post(self, body):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'key={key}'
        }
        response = requests.post(self.url, data=json.dumps(body), headers=headers)
        return response.json()

    def send(self, user_token: str, title, body='', to=None):
        data = {
            "to": user_token,
            "notification": {
                "body": body,
                "title": title,
            }
        }
        return self.post(data)
