from rest_framework import viewsets
from .models import Student, Candidate
from .serializers import StudentSerializer, CandidateSerializer
from rest_framework.views import exception_handler


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
