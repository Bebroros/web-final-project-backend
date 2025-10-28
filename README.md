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

## Headers

`Authorization: Bearer {token}`

## Endpoints
<hr>

### Events
Available only for authorized users, otherwise 403.


| Method   | Endpoint       | Description                                   | Response status                                 | Request body                                                                                                                                                                                                               | Response body                                                                                                                                                                                                                                                 |
| -------- | -------------- | --------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`    | `/events`      | get list of events for the authenticated user | `200`                                           | -                                                                                                                                                                                                                          | [  <br> {   <br> "id":1,<br>"title":"Meeting",<br>"description": "Meeting to do this..." ,<br>"appr_minutes_todo": 30,<br>"importance": 5, <br>"start_at":"2025-10-26 09:15",<br>"end_at": "2025-10-27 03:15",<br>"notify_before_min": 15 }, <br> ...]|
| `GET`    | `/events/{id}` | get full info about event                     | `200`, `404`(if not found)                      | -                                                                                                                                                                                                                          | {<br> "id":1,<br>"title":"Meeting",<br>"description": "Meeting to do this..." ,<br>"appr_minutes_todo": 30,<br> "importance": 5,<br>"start_at":"2025-10-26 09:15",<br> "end_at": "2025-10-27 03:15",<br>"notify_before_min": 15 <br>}                       |
| `POST`   | `/events`      | add new event in user`s calendar              | `201`, `400`(if bad request)                    | {<br>"title":"Meeting",<br>"description": "Meeting to do this..." ,<br>"appr_minutes_todo": 30,<br>"importance": 5, <br> "start_at":"2025-10-26 09:15",<br> "end_at": "2025-10-27 03:15",<br>"notify_before_min": 15 <br> } | {<br> "id":1,<br>"title":"Meeting",<br>"description": "Meeting to do this..." ,<br>"appr_minutes_todo": 30,<br> "importance": 5,<br>"start_at":"2025-10-26 09:15",<br> "end_at": "2025-10-27 03:15",<br>"notify_before_min": 15 <br> }                    |
| `PATCH`  | `/events/{id}` | partial updates on  specific event            | `200`, `404`(if not found), `400`(if bad request) | {  <br>"description": "Team Meeting to do ...",<br>"notify_before_min": 20}                                                                                                                                            | {<br>"id":1,<br>"title":"Meeting",<br>"description": "Team Meeting to do..." ,<br>"appr_minutes_todo": 30, <br> "importance": 5, <br>"start_at":"2025-10-26 09:15", <br>"end_at": "2025-10-27 03:15",<br>"notify_before_min": 20 <br> }                               |
| `DELETE` | `/events/{id}` | delete specific event                         | `204`, `404`(if not found)                      | -                                                                                                                                                                                                                          | -                                                                                                                                                                                                                                                             |

### Subscriptions
Available only for authorized users, otherwise 403.

| Method   | Endpoint              | Description                                                | Response status                                 | Request body                                                                                            | Response body                                                                                                                                                                           |
| -------- | --------------------- | ---------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GET`    | `/subscriptions`      | Get a list of all subscriptions for the authenticated user | `200`                                           | -                                                                                                       | [  <br>  {    <br>  "id": 1,<br>  "name": "Spotify",<br>  "payment_date": "2025-10-26",<br>  "cost": 5,<br>  "cycle": "monthly" <br>  },    <br>  ...<br>  ]|
| `GET`    | `/subscriptions/{id}` | get full info about subscription                           | `200`, `404`(if not found)                      | -                                                                                                       | {    <br>  "id": 1,<br>  "name": "Spotify",<br>  "payment_date": "2025-10-26",<br>  "cost": 5,<br>  "cycle": "monthly" <br>  }                                                          |
| `POST`   | `/subscriptions`      | add new subscription  to user`s list                       | `201`, `400`(if bad request)                    | {    <br>  "name": "Spotify",<br>"payment_date": "2025-10-26",<br>  "cost": 5,<br>  "cycle": "monthly" <br>  } | {    <br>  "id": 1,<br>  "name": "Spotify",<br>  "payment_date": "2025-10-26",<br>  "cost": 5,<br>  "cycle": "monthly" <br>  }                                                          |
| `PATCH`  | `/subscriptions/{id}` | partial updates on  specific subscription                  | `200`, `404`(if not found), `400`(if bad request) | {<br>"cost": 10<br>}                                                                                  | {    <br>  "id": 1,<br>  "name": "Spotify",<br>"payment_date": "2025-10-26",<br>  "cost": 10,<br>  "cycle": "monthly" <br>  }                                                           |
| `DELETE` | `/subscriptions/{id}` | delete specific event                                      | `204`, `404`(if not found)                      | -                                                                                                       | -                                                                                                                                                                                       |

### Auth
| Method   | Endpoint       | Description            | Response status                                  | Request body                                                                                                                                                                                                         | Response body                                                                                                                              |
| -------- |----------------|------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `POST` |` /auth/register` | Register a new account | `201`, `400`(if bad request)                      | {<br>"username": "artem",<br>"email": "artem@gmail.com",<br>"date": "10.06.2000", <br>"password": "password",<br>"password2": "password",<br>(optional)"first_name": "artem",<br>(optional)"second_name": "ber"<br>} | {<br>"username": "artem",<br>"email": "artem@gmail.com",<br>"date": "10.06.2000", <br>"password": "password",<br>"password2": "password",<br>"first_name": "artem",<br>"second_name": "ber", <br>} |
| `POST` | `/auth/login`    | Get a JWT token        | `200`, `400`(if bad request)                      | {<br>"username": "artem", <br>"password": "password", <br>}                                                                                                                                                          | {<br>"access": "...", <br>"refresh": "...", <br>}                                                                                          |
| `POST` | `/auth/refresh`  | Refresh a JWT token    | `200`, `400`(if bad request), `401`(if login failed) | {<br>"refresh": "...",<br>}                                                                                                                                                                                          | {<br>"access": "...",<br>}                                                                                                                 |


### User
Available only for authorized users, otherwise 403.

| Method | Endpoint | Description | Response status | Request body                      | Response body                                                                                                                                 |
|--------| ----------- | ----------- |-----|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `GET`    | `/user/{id}` | Get user info | `200` | -                                 | {<br>"username": "artem",<br>"email": "artem@gmail.com", <br>"date": "10.06.2000",<br>"first_name": "artem",<br>"second_name": "ber"<br>}                              |
| `PATCH`  | `/user/{id}` | Update user info | `200`, `400`(if bad request) | {<br>"username": "artem123",<br>} | {<br>"username": "artem123",<br>"email": "artem@gmail.com", <br>"date": "10.06.2000", <br>"first_name": "artem",<br>"second_name": "ber"<br>} |

### Astrology
Available only for authorized users, otherwise 403.

| Method | Endpoint           | Description                      | Response status                  | Request body                      | Response body                                                                                                       |
|--------|--------------------|----------------------------------|----------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `GET`  | `/astrology/daily`   | Get daily astrology prediction   | `200`                             | - | {<br>"prediction": "..."<br>} |
| `GET`  | `/astrology/finance` | Get finance astrology prediction | `200`                             | - | {<br>"prediction": "..."<br>} |
| `GET`  | `/astrology/love`    | Get love astrology prediction    | `200`                              | - | {<br>"prediction": "..."<br>} |

## Database

<img width="979" height="524" alt="image" src="https://github.com/user-attachments/assets/c5e0e2af-c2ab-452c-b4c3-89ff9d83f332" />
