from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import AlarmEvent
from .serializers import AlarmEventSerializer
from django.utils.timezone import now
import random
from datetime import datetime

def generateRandomDate():
    year = random.choice(range(1950, 2001))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    return datetime(year,month,day)


class AlarmAPIBaseTest(APITestCase):
    client = APIClient()

    @staticmethod
    def createAlarm(AlarmName = "",AlarmTime = now(),Alarmkilled = None):
        AlarmEvent.objects.create(
            AlarmName=AlarmName, AlarmTime=AlarmTime, AlarmKilled=Alarmkilled
        )

    def setUp(self):

        self.createAlarm("Office")
        self.createAlarm("Home", generateRandomDate(), generateRandomDate())
        self.createAlarm("Test", generateRandomDate(), generateRandomDate())
        self.createAlarm("Test II", generateRandomDate(), generateRandomDate())

class ShowAllAlarmsTest(AlarmAPIBaseTest):

    def test_show_all_alarms(self):
        response = self.client.get(
            reverse("alarms")
        )
        expected = AlarmEvent.objects.all()
        serialized = AlarmEventSerializer(expected,many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)