from django.contrib import admin

# Register your models here.
from .models import Messages,Chat

admin.site.register(Messages)
admin.site.register(Chat)
