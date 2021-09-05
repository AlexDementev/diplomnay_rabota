from django.contrib import admin

# Register your models here.
from pages.models import Product, MyUser

admin.site.register(Product)
admin.site.register(MyUser)