from django.urls import path
from message_ import views

urlpatterns = [
    path('send_message/', views.send_message.as_view(), name='send_message'),

    path('send_link/', views.send_link.as_view(), name='send_link'),

    path("reply_text/", views.text_reply.as_view(), name='reply_'),

    path('campaigns/', views.Campaigns.as_view(), name='campaign'),

    path('send_message_indi/', views.send_message_individually.as_view(), name='send_message_individually'),
    path('templates/', views.templates.as_view(), name='templates'),
    path('contacts/', views.contacts.as_view(), name='contacts'),
    path('unique/', views.UniqueTagsAndAddressesView.as_view(), name='unique'),
    path('fe1ef8f2-4a7c-4502-a8d7-a59162d3fa17/', views.WhatsApp_Webhook.as_view(), name='send_message_webhook'),
]   


#urls = http://095f-2409-40e3-3156-a73c-c23-975-12ab-9e4c.ngrok-free.app/message/fe1ef8f2-4a7c-4502-a8d7-a59162d3fa17/
# verify token = d64bb6cc-dc1a-4e78-ae7f-1521c8836307
#1013378269999323