from django.contrib import admin
from message_.models import replies, Templates, Media, Contact

# Register your models here.

admin.site.register(replies)
admin.site.register(Templates)
admin.site.register(Media)
admin.site.register(Contact)


