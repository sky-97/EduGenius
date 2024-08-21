from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutView, MeView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', MeView.as_view(), name='me'),
    # path('check-token/', CheckTokenView.as_view(), name='check_token'),
]
