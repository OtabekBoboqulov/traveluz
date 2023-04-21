from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Countries)
admin.site.register(Languages)
