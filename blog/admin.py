from django.contrib import admin
from .models import Post
from .models import ContactMessage


# Register your models here.
admin.site.register(Post)

admin.site.register(ContactMessage)