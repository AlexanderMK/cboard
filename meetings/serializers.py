from rest_framework import serializers

from meetings.models import Participant, Meetings
class ParticipantSerializer(serializers.ModelSerializer):
   class Meta:
       model = Participant
       fields = ('firstName', 'middleName', 'lastName', 'phoneNumber')


class MeetingsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Meetings
       fields = ('title', 'time', 'location')