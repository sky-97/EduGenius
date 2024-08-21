from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TutoringSessionViewSet

router = DefaultRouter()
router.register(r'sessions', TutoringSessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
