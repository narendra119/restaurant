from django.contrib import admin
from core.models import Customer, Orders, Payments

# Register your models here.
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Payments)