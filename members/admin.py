from django.contrib import admin
from .models import Welcome

class MemberAdmin(admin.ModelAdmin):
    list_display =("name","Age",)

admin.site.register(Welcome , MemberAdmin)
# Register your models here.
