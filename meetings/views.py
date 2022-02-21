from django.shortcuts import render
from rest_framework import viewsets

from meetings.serializers import ParticipantSerializer, MeetingsSerializer
from meetings.models import Participant, Meetings

# Create your views here.

class ParticipantViewSet(viewsets.ModelViewSet):
   queryset = Participant.objects.all()
   serializer_class = ParticipantSerializer


class MeetingsViewSet(viewsets.ModelViewSet):
   queryset = Meetings.objects.all()
   serializer_class = MeetingsSerializer
