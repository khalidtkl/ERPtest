from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Country)
admin.site.register(City)
admin.site.register(ContactType)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(AddressType)
admin.site.register(Employee)
admin.site.register(Document)