from curses.ascii import US
from django.contrib import admin
from .models import Item
# from .models import User

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'image','userImage','user', 'location' ,'rating' ,'title', 'item' ,'size' ,'brand' ,'description', 'show')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')

# Register your models here.

admin.site.register(Item, ItemAdmin)
# admin.site.register(User, UserAdmin)
