from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from message_.utils import send
import json
# Create your views here.



class send_message(APIView):
    def post(self, request):
        rev = request.POST.get('to_number')
        print(rev)
        temp = request.POST.get('templates')
        res = send.send_message(rev, temp)
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
        print(request)
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
                        message = '{0}, {1}'.format(text, profile_name)
                        send.send_message_individual(phone_Number, message)
                except:
                    pass
        return HttpResponse("success", status=200)