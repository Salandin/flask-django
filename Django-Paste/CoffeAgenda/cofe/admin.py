from django.contrib import admin
from cofe.models import Envento
# Register your models here.

class EnventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','id','date_event','usuario_id')
    list_filter = ('usuario','date_event',)

admin.site.register(Envento, EnventoAdmin)