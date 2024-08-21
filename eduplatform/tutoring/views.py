from rest_framework import viewsets
from .models import TutoringSession
from .serializers import TutoringSessionSerializer

class TutoringSessionViewSet(viewsets.ModelViewSet):
    queryset = TutoringSession.objects.all()
    serializer_class = TutoringSessionSerializer
