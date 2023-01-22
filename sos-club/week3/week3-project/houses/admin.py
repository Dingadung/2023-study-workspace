from django.contrib import admin

from .models import House
from .models import Todo

# Register your models here.


class HouseAdmin(admin.ModelAdmin):
	pass

admin.site.register(House)

class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo)