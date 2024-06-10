from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(aadhar)
class aadharadmin(admin.ModelAdmin):
    list_display = ['aadhar_number','full_name','date_of_birth','father_name','phone_number']
    
@admin.register(voterregister)
class VoterRegisterAdmin(admin.ModelAdmin):
    list_display = ['aadhar_number','password']
    
@admin.register(mlapolling)
class MlaAdmin(admin.ModelAdmin):
    list_display=['MLA_name', 'user']
    
@admin.register(mppolling)
class MpAdmin(admin.ModelAdmin):
    list_display=['MP_name','user']