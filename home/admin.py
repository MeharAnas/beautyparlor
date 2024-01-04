from django.contrib import admin
from .models import*
# Register your models here.
class BoodkingAdmin(admin.ModelAdmin):
      list_display = ('Name','Email','Number','Category','Date','Message')
admin.site.register(Booking,BoodkingAdmin)