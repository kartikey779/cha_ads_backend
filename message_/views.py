from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from message_.utils.send import Reply_Response, Message_Response
import json
from message_.models import replies, Templates, Media, Contact
import datetime
from message_.api.serializers import template_serializer, Contacts_serializer
from django.http import JsonResponse

# Create your views here.

temp_data = Templates.objects.all()
class send_message(APIView):
    def post(self, request):
        rev = request.POST.get('to_number')
        temp = request.POST.get('templates')
        b = Message_Response()
        res = b.send_message(to_number=rev, templates=temp)
        return JsonResponse(res)

class send_link(APIView):
    def post(self, request):
        print(request.POST)
        phone_number = request.POST.get('phone_number')
        link = request.POST.get('link')
        res = send.send_link(phone_number, link)
        return JsonResponse(res)

class send_message_individually(APIView):
    def post(self, request):
        phone_number = request.POST.get('to_number')
        message = "Hello there, \n This is our first Django WhatsApp message"
        res = send.send_message_individual(phone_number, message)
        return JsonResponse(res)
    

class WhatsApp_Webhook(APIView):
    def get(self, request):
        verify_token = "d64bb6cc-dc1a-4e78-ae7f-1521c8836307"
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")
        
        if mode == "subscribe" and token == verify_token:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse("error", status=403)
        

     
    def post(self, request):
        data = json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        phone = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phone_id = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profile_name = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        messageId = entry['changes'][0]['value']['messages'][0]['id']
                        timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body'] 
                        phone_Number = whatsAppId
                        date = datetime.datetime.now()
                        b = replies(customer=profile_name,message=text, date=date)
                        b.save()
                        
                        temp_message = template_serializer(temp_data,many=True).data


                        if text.lower() == 'send':
                            message = temp_message[0].get("template_message")
                            formatted_message = message.replace("\\n", "\n")
                            b = Message_Response()
                            d = Reply_Response()
                            emoji = "👍"
                            numbers = ["919580266938","919305619760"]
                            #mark as read 
                            b.Mark_as_read(message_id=messageId)
                            #emoji reaction
                            d.send_emoji_reply(phone_number=phone_Number,message_id=messageId,emoji=emoji)
                            #send message to selected contacts
                            b.send_bulk_message(message=formatted_message, phone_numbers=numbers) 

                        if text.lower() == 'get':
                            b = Message_Response()
                            img = "1013378269999323"
                            c = b.get_media(phone_number_id=phone_id, image_id=img)
                            url = c.get('url')
                            img_id = c.get('id')
                            print(url)
                            dow = b.download_media(img_url=c.get('url'))
                            print(c)
                            print(dow)
                            med = Media(url=url,img_id=img_id)
                            med.save()

                            

                            b.send_link(phone_number=phone_Number,link=c.get('id'))
                        

                        if text.lower() == 'delete':
                            b = Message_Response()
                            img = "1664025064417484"
                            b.delete_image(phone_number_id=phone_id,image_id=img)
                        
                        if text.lower() == 'hi':
                            message = temp_message[0].get("template_message")
                            formatted_message = message.replace("\\n", "\n")
                            emoji = "👍"
                            d = Reply_Response()
                            b = Message_Response()
                            b.Mark_as_read(message_id=messageId)
                            d.send_emoji_reply(phone_number=phone_Number, message_id=messageId,emoji=emoji)
                            img = "1013378269999323"
                            # b.send_image_reply(phone_number=phone_Number,message_id=messageId,image_id=img)
                            # b.send_image(phone_number=phone_Number, image_id=img)
                            # d.send_emoji_reply(phone_number=phone_Number, message_id=messageId, emoji=emoji)

                            header_text = "Hi  919580266938,"
                            body_text = "This is Delhi Metro Autometic\n Reply Chatbot.\n You can buy DMRC and \nAirport Express Line \nTicket here! \nPlease Choose your preferred language."
                            footer_text = "1.Hindi \n 2.English"
                            button_text = "first"
                            # d.send_reply_to_list_of_messages(phone_number=phone_Number, message_id=messageId, header_text=header_text, body_text=body_text, footer_text=footer_text, button_text=button_text)

                            body_content = "Hello, World This help you select in two buttons:"
                            button_one_name = "option1"
                            button_two_name = "option2"
                            # b.send_button_reply(phone_number=phone_Number, body_content=body_content,button_one_name=button_one_name,button_two_name=button_two_name)
                            # d.send_product_message(phone_number=phone_Number)
                            d.send_text_reply(phone_number=phone_Number, message_id=messageId,message=formatted_message)
                            # send.send_message_individual(phone_Number, formatted_message)
                        else:
                            if text == '1':
                                message = "हिंदी"
                                send.send_message_individual(phone_Number, message)
                            if text == '2':
                                message = "English"
                                messageT = temp_message[1].get("templates")
                                formatted_message = messageT.replace("\\n", "\n")
                                send.send_message_individual(phone_Number, message)
                                mesage_set = "Please Select one of the options \n below to start.😊 \n \n 3.Buy Ticket \n 4. Smart Card TopUp \n 5. Retrieve Ticket \n \n Tap below 👇 to explore more \n Services \n \n 6.Select Here"
                                send.send_message_individual(phone_Number, formatted_message)
                            if text == '3':
                                message = "https://waf-five.vercel.app/"
                                send.send_message_individual(phone_Number, message) 
                except:
                    pass
        return HttpResponse("success", status=200)
    
class templates(APIView):
    
    def post(self, request):
        template_name = request.data.get("template_name")
        template_type = request.data.get("template_type")
        templates_message = request.data.get("templates_message")
        temp_message = templates_message.replace("/","\\")
        b = Templates(template_name=template_name, template_type=template_type, template_message=temp_message)
        b.save()
        return HttpResponse("success", status=200)

    def get(self, request):
        temp_data = Templates.objects.all()
        d = template_serializer(temp_data, many=True)
        length = len(d.data)
        for i in range(length):
            d.data[i]['template_message'] = d.data[i]['template_message'].replace("\\n","/n")
        return JsonResponse(d.data,safe=False)


class text_reply(APIView):
    
    def post(self, request):
        data = json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        messageId = entry['changes'][0]['value']['messages'][0]['id']
                        whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        message = "what"
                        send.send_text_reply(whatsAppId,message_id=messageId,message=message)
                except:
                    pass
        return HttpResponse("success", status=200)

class contacts(APIView):
    def post(self, request):
        name = request.data.get('name')
        phone_number = request.data.get('phone')
        address = request.data.get('address')
        tags = request.data.get('tags')
        contact = Contact(name=name, phone_number=phone_number, address=address, tags=tags)
        contact.save()
        return HttpResponse("success", status=200)


    def get(self, request):
        contacts = Contact.objects.all()
        serializer = Contacts_serializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)

class UniqueTagsAndAddressesView(APIView):
    def get(self, request):
        # Retrieve all UserData objects
        contacts = Contact.objects.all()
        
        templates = Templates.objects.all()

        unique_templates = set(templates.values_list('template_name', flat=True))
        # Extract unique addresses
        unique_addresses = set(contacts.values_list('address', flat=True))
        
        # Extract unique tags
        unique_tags = set()
        for contact in contacts:
            unique_tags.update(contact.tags)
        
        # Return the unique addresses and tags as JSON response
        return JsonResponse({
            'unique_templates': list(unique_templates), 
            'unique_addresses': list(unique_addresses),
            'unique_tags': list(unique_tags)
        })

class Campaigns(APIView):

    def post(self, request):
        # retriving address from request
        address = request.data.get('selectedAddress')
        # retriving template from request
        template_name = request.data.get('selectedTemplate')
        # retriving tags from request
        tags = request.data.get('selectedTag')

        template = Templates.objects.filter(template_name=template_name)

        # serializing template data to get message for bulk sending
        serializer_template = template_serializer(template,many=True)
        message = ""
        for template_data in serializer_template.data:
             message += template_data.get('template_message', '') + " "
        message = message.strip()
        formated_message = message.replace("\\n","\n ")

        # retriving contacts from database
        if tags:
            contacts = Contact.objects.filter(tags__0=tags)
        if address:
            contacts = Contact.objects.filter(address=address)
        
        # contacts = Contact.objects.filter(address=address)
        serializer_contact = Contacts_serializer(contacts,many=True)
        phone_numbers = []
        for contact_data in serializer_contact.data:
            phone_numbers.append(contact_data.get('phone_number'))
        print(phone_numbers)
        #sending bulk message to numbers
        b = Message_Response()
        b.send_bulk_message(phone_numbers, formated_message)

        return JsonResponse({
            'data': 'Campaign created successfully'
        })