# tutoring/admin.py

from django.contrib import admin
from .models import TutorSession

@admin.register(TutorSession)
class TutorSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_time', 'end_time')  # Ensure these fields exist in the model
    search_fields = ('name',)
