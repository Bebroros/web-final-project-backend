# Calendar
## Team
- Artem Shkilniuk: Bebroros
- Vysokovskykh Kateryna: Kvstkk

## How to start

1. crontab -e 
2. enter this to crontab: `\* \* \* \* \* [python_path] [calendar_project_path]/manage.py notifications >> [calendar_project_path]/cron.log 2>&1`
3. python manage.py runserver


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

## Database

<img width="979" height="524" alt="image" src="https://github.com/user-attachments/assets/c5e0e2af-c2ab-452c-b4c3-89ff9d83f332" />
