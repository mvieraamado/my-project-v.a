from django.contrib import admin

from clase.models import BlogPosts, Client_n, Manicurist, Turn

# Register your models here.
admin.site.register(Manicurist)
admin.site.register(Client_n)
admin.site.register(Turn)
admin.site.register(BlogPosts)