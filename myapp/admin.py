from django.contrib import admin
from myapp.models import Orders
from myapp.models import Contacts

# Register your models here.
admin.site.register(Orders)
admin.site.register(Contacts)