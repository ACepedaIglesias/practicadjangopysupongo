from django.contrib import admin

from app.models import Proveedor, Topping, Pizza

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Topping)
admin.site.register(Pizza)
