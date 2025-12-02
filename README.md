# Calendar
## Team
- Artem Shkilniuk: Bebroros
- Vysokovskykh Kateryna: Kvstkk

## How to start

1. pip install -r requirements.txt
2. crontab -e 
3. enter this to crontab: `* * * * * [python_path] [calendar_project_path]/manage.py event_notifications >> [calendar_project_path]/cron.log 2>&1`
4. enter this to crontab: `0 12 * * * [python_path] [calendar_project_path]/manage.py sub_notifications >> [calendar_project_path]/cron.log 2>&1`
5. python manage.py runserver


## Description
Calendar which allows you to: 
- add events
- set up notifications
- manage your subscriptions
- get astrological predictions.

<hr>

## Headers

`Authorization: Bearer {token}`

## Endpoints
<hr>

You can view all endpoints at http://127.0.0.1:8000/swagger

## Tests

pytest [project]/prcalendar/test/test*

## Database

<img width="712" height="629" alt="image" src="https://github.com/user-attachments/assets/37a18cea-608e-4fd7-b39f-1066cfa2f0cc" />
