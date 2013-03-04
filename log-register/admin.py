from django.contrib import admin
from log_register.models import Lot, Log


class LotAdmin(admin.ModelAdmin):
    pass


class LogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lot, LotAdmin)
admin.site.register(Log, LogAdmin)

__author__ = 'leandro'
