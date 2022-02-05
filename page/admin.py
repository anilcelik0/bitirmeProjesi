from django.contrib import admin
from page.models import yer

# Register your models here.
class yerAdmin(admin.ModelAdmin):
    list_display = ("yerVeri","neredeVeri")

admin.site.register(yer,yerAdmin)