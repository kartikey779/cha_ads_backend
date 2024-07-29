import requests

url = "https://graph.facebook.com/v20.0/372273929306076/messages"
token = "EAAHYD3KyxJQBOZCGhJn0XOvm5GlYgMaU30J1wdDreJi1otFtx2OOAGdwvwv4KZAXeaqJT02xlZCNnl8JTy171gALZBtYfKK4aTh9sHBdbJTOZBvSBYqO902pgAOlNqW7IRZCEQepSL2bdQguY5U4iL88ec6i43H66oLhASiMWsvZCnqBgbxPh7oLKJ75l6Rx4FQgYhAQZCODtwu77Qnuy3UZD"
def send_message(to_number, templates):
    
    headers = {
        'Authorization': f'Bearer {0}'.format(token),
        'Content-Type': 'application/json'
        }
    payload = {
        "messaging_product": "whatsapp",
        "to":"91" + to_number,
        "type": "template",
        "template": {
            "name": templates,
            "language": {
                "code": "en_US"
            }
        }
    }
    response = requests.post(url, json=payload,headers=headers)
    return response.json()

def send_message_individual(phone_number, message):
    headers = {
        "Authorization": 'Bearer {}'.format(token),
    }
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,
        "type": "text",
        "text": { "body": message }
    }
    response = requests.post(url, headers=headers, json=payload)
    ans = response.json()
    return ans

# phone_number = "919580266938"
# message = "Hello there, \n This is our first Django WhatsApp message"
    