from django.urls import path
from message_ import views

urlpatterns = [
    path('send_message/',views.send_message.as_view(), name='send_message'),
    path('send_message_indi/',views.send_message_individually.as_view(), name='send_message_individually'),
    path('fe1ef8f2-4a7c-4502-a8d7-a59162d3fa17/',views.WhatsApp_Webhook.as_view(), name='send_message_webhook'),
    
]   


#urls = http://ef89-2409-40e3-54-3b9b-f92c-f769-1ed5-33a1.ngrok-free.app /message/fe1ef8f2-4a7c-4502-a8d7-a59162d3fa17/
# verify token = d64bb6cc-dc1a-4e78-ae7f-1521c8836307