from django.contrib import admin
from django.urls import path, include

# google calendar app module
from google_calendar.views import (
        GoogleCalendarInitView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest/v1/calendar/init/', GoogleCalendarInitView, name="googlecalendarinit" ),
]   

