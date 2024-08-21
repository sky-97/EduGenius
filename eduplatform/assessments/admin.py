# assessments/admin.py
from django.contrib import admin
from .models import Assessment, Question

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')  # Ensure these fields exist on the Assessment model

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'assessment', 'points')  # Ensure these fields exist on the Question model
