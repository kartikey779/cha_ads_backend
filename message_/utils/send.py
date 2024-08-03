import requests

url = "https://graph.facebook.com/v20.0/372273929306076/messages"
token = "EAAHYD3KyxJQBO7cZC9jHuLXan5n3XZCOf9oxGpVM2onGA82YGnnlIWAKtA3ZCZAExrzrep4lI8hi8ftYoehfi6K3bnGBmeNypAC9E0Tc51FG1igPQOJq9vgUcC8y2TEeZBDzd1WrMJznZApG3zyMKu00bf3cZBqicq3EnfzHa62YryiDAcChV1OeztBZCaEZBhOndzcak06QaP8RaWDrbNZAUZD"


class Message_Response:

    #sending custom  message if customer replied
    def send_message_individual(self, phone_number, message):
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
    #sending custom message with link if customer replied
    def send_link(self,phone_number,link):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "text": {
                "preview_url": True,
                "body": link
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()


    #sending with custom templates message
    def send_message(self,to_number, templates):
        headers = {
            'Authorization': 'Bearer {0}'.format(token),
        }
        payload = {
            "messaging_product": "whatsapp",
            "to":to_number,
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

    # sending message reply through image
    def send_image_reply(self, phone_number, image_id):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "image",
            "image": {
                "id": image_id
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    # sending button reply to text message
    def send_button_reply(self, phone_number, body_content, button_one_name, button_two_name):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": body_content
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_1>",
                                "title": button_one_name
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_2>",
                                "title": button_two_name
                            }
                        }
                    ]
                }
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    

    
    #sending product to customers
    def send_product_message(self, phone_number):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "interactive",
            "interactive": {
                "type": "product",
                "body": {
                    "text": "<OPTIONAL_BODY_TEXT>"
                },
                "footer": {
                    "text": "<OPTIONAL_FOOTER_TEXT>"
                },
                "action": {
                    "catalog_id": "367025965434465",
                    "product_retailer_id": "<ID_TEST_ITEM_1>"
                }
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    # sending catalog message to customers
    def send_catalog_message(self, phone_number):
        headers = headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "interactive",
            "interactive": {
                "type": "catalog_message",
                "body": {
                    "text": "Hello! Thanks for your interest. Ordering is easy. Just visit our catalog and add items to purchase."
                },
                "action": {
                    "name": "catalog_message",
                    "parameters": {
                        "thumbnail_product_retailer_id": "2lc20305pt"
                    }
                },
                "footer": {
                    "text": "Best grocery deals on WhatsApp!"
                }
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    #making message mark as read 
    def Mark_as_read(self, message_id):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id": message_id
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()




class Reply_Response:
    #send reply with text message
    def send_text_reply(self, phone_number,message_id, message):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload ={
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "context":{
                "message_id": message_id
            },
            "type":"text",
            "text": {
                "preview_url": False,
                "body": message
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def send_emoji_reply(self, phone_number, message_id,emoji):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "reaction",
            "reaction": {
                "message_id": message_id,
                "emoji": emoji
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    
    # sending reply to list of messages
    def send_reply_to_list_of_messages(self, phone_number, message_id, header_text, body_text, footer_text, button_text ):
        headers = {
            'Authorization': 'Bearer {}'.format(token),
            'content-type': 'application/json'
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "context": {
                "message_id": message_id
            },
            "type": "interactive",
            "interactive": {
                "type": "list",
                "header": {
                    "type": "text",
                    "text": header_text
                },
                "body": {
                    "text": body_text
                },
                "footer": {
                    "text": footer_text
                },
                "action": {
                    "button": button_text,
                    "sections": [
                        {
                            "title": "<LIST_SECTION_1_TITLE>",
                            "rows": [
                                {
                                    "id": "<LIST_SECTION_1_ROW_1_ID>",
                                    "title": "<SECTION_1_ROW_1_TITLE>",
                                    "description": "<SECTION_1_ROW_1_DESC>"
                                },
                                {
                                    "id": "<LIST_SECTION_1_ROW_2_ID>",
                                    "title": "<SECTION_1_ROW_2_TITLE>",
                                    "description": "<SECTION_1_ROW_2_DESC>"
                                }
                            ]
                        },
                        {
                            "title": "<LIST_SECTION_2_TITLE>",
                            "rows": [
                                {
                                    "id": "<LIST_SECTION_2_ROW_1_ID>",
                                    "title": "<SECTION_2_ROW_1_TITLE>",
                                    "description": "<SECTION_2_ROW_1_DESC>"
                                },
                                {
                                    "id": "<LIST_SECTION_2_ROW_2_ID>",
                                    "title": "<SECTION_2_ROW_2_TITLE>",
                                    "description": "<SECTION_2_ROW_2_DESC>"
                                }
                            ]
                        }
                    ]
                }
            }
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()


    
# phone_number = "919580266938"
# message = "Hello there, \n This is our first Django WhatsApp message"
    