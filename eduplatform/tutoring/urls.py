from django.urls import path
from .views import TutoringSessionListView

urlpatterns = [
    path('', TutoringSessionListView.as_view(), name='tutoring-session-list'),
]
