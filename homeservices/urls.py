from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'alarms/$', views.ListAlarmsView.as_view(), name='alarms'),
]