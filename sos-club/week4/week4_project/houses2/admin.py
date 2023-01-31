from django.contrib import admin
from .models import House2

# Register your models here.

@admin.register(House2)
class HouseAdmin(admin.ModelAdmin):
	pass