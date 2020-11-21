from django.contrib import admin

# Register your models here.
from myapp.models import UserDetails

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'password')