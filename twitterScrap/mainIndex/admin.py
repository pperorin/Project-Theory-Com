from django.contrib import admin
from .models import mainIndex
# Register your models here.
class MainIndexAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

admin.site.register(mainIndex, MainIndexAdmin)