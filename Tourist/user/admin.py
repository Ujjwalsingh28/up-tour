from django.contrib import admin

from . models import *

class contactAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Address','Subject','Message')
admin.site.register(contact,contactAdmin)

class tbl_galleryAdmin(admin.ModelAdmin):
    list_display=('id','picture')
admin.site.register(tbl_gallery,tbl_galleryAdmin)


class tbl_registerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'password', 'pincode', 'city', 'address')
admin.site.register(tbl_register, tbl_registerAdmin)