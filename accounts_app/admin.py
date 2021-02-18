from django.contrib import admin
from .models import CustomUser, Profile



admin.site.register(CustomUser)
admin.site.register(Profile)


class CustomUserAdmin(admin.ModelAdmin):
    fields = '__all__'
    list_editable = ['reserv2']















