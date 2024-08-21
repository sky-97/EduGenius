# tutoring/admin.py
from django.contrib import admin
from .models import TutoringSession

@admin.register(TutoringSession)
class TutoringSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')
