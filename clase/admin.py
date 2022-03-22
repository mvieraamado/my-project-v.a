from django.contrib import admin

from clase.models import Client_n, Manicurist, Turn

# Register your models here.
admin.register(Manicurist)
admin.register(Client_n)
admin.register(Turn)