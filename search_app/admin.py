from django.contrib import admin
from .models import Dish

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')

admin.site.register(Dish, DishAdmin)
