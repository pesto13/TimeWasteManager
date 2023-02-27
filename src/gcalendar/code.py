from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
# import datetime
# import pytz

# Carica le credenziali dal file JSON
creds = Credentials.from_authorized_user_file('path/to/credentials.json')

# Costruisci l'oggetto per accedere all'API di Google Calendar
service = build('calendar', 'v3', credentials=creds)

# Esempio: crea un evento nel calendario
event = {
  'summary': 'Test event',
  'location': 'Rome, Italy',
  'description': 'A simple test event',
  'start': {
    'dateTime': '2023-02-28T09:00:00+01:00',
    'timeZone': 'Europe/Rome',
  },
  'end': {
    'dateTime': '2023-02-28T10:00:00+01:00',
    'timeZone': 'Europe/Rome',
  },
  'reminders': {
    'useDefault': True,
  },
}

try:
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
except HttpError as error:
    print('An error occurred: %s' % error)
