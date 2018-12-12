from django.contrib import admin
from .models import Status
from .forms import StatusForm

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
	form = StatusForm

admin.site.register(Status,StatusAdmin)
