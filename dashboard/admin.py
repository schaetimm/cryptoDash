from django.contrib import admin
from .models import Broker


# Register your models here.

class BrokerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'date')
    search_fields = ('name', 'url')
    list_filter = ('date',)


admin.site.register(Broker, BrokerAdmin)
