# Calendar
## Team
- Artem Shkilniuk: Bebroros
- Vysokovskykh Kateryna: Kvstkk

## Description
Calendar which allows you to: 
- add events
- set up notifications
- manage your subscriptions
- get astrological predictions.

<hr>

## Endpoints

### Events

#### all events
- **Request**: ```GET /events```
- **Purpose**:  get list of events for the authenticated user
- **Response status**: ```200 OK```
- **Response body**: 
```
[
 {
    "id":1,
    "title":"Meeting",
    "description": "Meeting to do this..." ,
    "appr_minutes_todo": 30,
    "importance": 5,
    "start_at":"2025-10-26 09:15",
    "end_at": "2025-10-27 03:15",
    "notify_before_min": 15
 },
    ...
]
```
#### specific event
- **Request**: ```GET /events/1```
- **Purpose**:  get full info about event
- **Response status**: ```200 OK``` 
- **Response body**: 
```
{
	"id":1,
	"title":"Meeting",
	"description": "Meeting to do this..." ,
	"appr_minutes_todo": 30,
	"importance": 5,
	"start_at":"2025-10-26 09:15",  
	"end_at": "2025-10-27 03:15",
	"notify_before_min": 15
}
```
#### create new  event
- **Request**: ```POST /events```
- **Purpose**:  add new event in user`s calendar
- **Response status**: ```201 Created```
- **Request body**: 
```
{
	"title":"Meeting",
	"description": "Meeting to do this..." ,
	"appr_minutes_todo": 30,
	"importance": 5,
	"start_at":"2025-10-26 09:15",  
	"end_at": "2025-10-27 03:15",
	"notify_before_min": 15
}
```
- **Response body**: 
```
{
	"id":1,
	"title":"Meeting",
	"description": "Meeting to do this..." ,
	"appr_minutes_todo": 30,
	"importance": 5,
	"start_at":"2025-10-26 09:15",  
	"end_at": "2025-10-27 03:15",
	"notify_before_min": 15
}
```
#### update  event
- **Request**: ```PATCH /events/1```
- **Purpose**:  partial updates on  specific event
- **Response status**:  ``200 OK``

**Request body**: 
```
{
	"description": "Team Meeting to do this..." ,
	"notify_before_min": 20
}
```
- **Response body**: 
```
{
	"id":1,
	"title":"Meeting",
	"description": "Team Meeting to do this..." ,
	"appr_minutes_todo": 30,
	"importance": 5,
	"start_at":"2025-10-26 09:15",  
	"end_at": "2025-10-27 03:15",
	"notify_before_min": 20
}
```
#### delete  event
- **Request**: ```DELETE /events/1```
- **Purpose**:  delete specific event
- **Response status**: ```204 No Content```
<hr>

### Subscriptions

#### all subscriptions
- **Request**: ```GET /subscriptions```
- **Purpose**:  Get a list of all subscriptions for the authenticated user
- **Response status**: ```200 OK```
- **Response body**: 
```
[
  {
    "id": 1,
    "name": "Spotify",
    "payment_date": "2025-10-26",
    "cost": 5,
    "cycle": "monthly"
  },
	..
]
```
#### specific subscription
- **Request**: ```GET /subscriptions/1```
- **Purpose**:  get full info about subscription
- **Response status**: ```200 OK``` 
- **Response body**: 
```
  {
    "id": 1,
    "name": "Spotify",
    "payment_date": "2025-10-26",
    "cost": 5,
    "cycle": "monthly"
  }
```
#### create new  subscription
- **Request**: ```POST /subscriptions```
- **Purpose**:  add new subscription  to user`s list
- **Response status**: ```201 Created```
- **Request body**: 
```
  {
    "name": "Spotify",
    "payment_date": "2025-10-26",
    "cost": 5,
    "cycle": "monthly"
  }
```
- **Response body**: 
```
  {
    "id": 1,
    "name": "Spotify",
    "payment_date": "2025-10-26",
    "cost": 5,
    "cycle": "monthly"
  }
```
#### update  subscription
- **Request**: ```PATCH /subscriptions/1```
- **Purpose**:  partial updates on  specific subscription
- **Response status**:  ``200 OK``
- **Request body**: 
```
  {
    "cost": 10
  }

```
- **Response body**: 
```
  {
    "id": 1,
    "name": "Spotify",
    "payment_date": "2025-10-26",
    "cost": 10,
    "cycle": "monthly"
  }

```
#### delete  subscription
- **Request**: ```DELETE /subscriptions/1```
- **Purpose**:  delete specific subscription
- **Response status**: ```204 No Content```
<hr>
