from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date")
    prepopulated_fields = {"slug": ("firstname", "lastname")}
    
admin.site.register(Member, MemberAdmin)