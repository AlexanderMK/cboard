from django.urls import include, path

from rest_framework import routers

from meetings.views import ParticipantViewSet, MeetingsViewSet

router = routers.DefaultRouter()
router.register(r'participants', ParticipantViewSet)
router.register(r'meetings', MeetingsViewSet)

urlpatterns = [
   path('admin/', include('meetings.urls')),
]
