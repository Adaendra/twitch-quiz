# Socket contracts

Description of all Socket requests and events available.

## Requests
### request:quiz:init
Request to initialize a quiz.
#### Body
*/*

---

## Events
### event:notification:send
Send a notification to the frontend clients.
#### Body
- **message** : Content of the notification
- **level** : Level of the notification. Values availables: INFO, WARNING, ERROR.

*exemple*
```json
{
    "message": "Error raised: xxx",
    "level": "ERROR"
}
```

<br/>
    
### event:contestants:check_in_stats
Send statistics about the Check-In.
#### Body
- **number_contestants** : Number of contestants registered

*exemple*
```json
{
    "number_contestants": 42
}
```