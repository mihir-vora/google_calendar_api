from django.shortcuts import render, redirect
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from decouple import config
import googleapiclient.discovery
import pickle
import datetime
from .calendar_API import test_calendar

CAL_ID = config('CAL_ID')
SCOPES = ['https://www.googleapis.com/auth/calendar']
FILE = 'google_calendar/client_secret.json'


def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'index.html', context)


def GoogleCalendarInitView(request):
    print("RUNNING TEST_CALENDAR()")
    flow = InstalledAppFlow.from_client_secrets_file(FILE, scopes=SCOPES)
    # take the url from terminal or cmd etc...
    credentials = flow.run_console()
    pickle.dump(credentials, open("token.pkl", "wb"))
    credentials = pickle.load(open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    # service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)
    print("Service", service)

    # CREATE A NEW EVENT
    new_event = {
    'summary': "Testing",
    'location': 'testing light',
    'description': 'https://testing.com',
    'start': {
        'date': f"{datetime.date.today()}",
        'timeZone': 'America/New_York',
    },
    'end': {
        'date': f"{datetime.date.today() + datetime.timedelta(days=3)}",
        'timeZone': 'America/New_York',
    },
    }

    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

    # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])
    for e in events:
        print(e)
    context = {
        'results' : events,
    }
    return render(request, index.html, context)

