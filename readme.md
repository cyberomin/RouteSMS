###RouteSMS
A modular API for interacting with the RouteSMS HTTP API

#####Usage
________

```python
sms = RouteSMS(username, password)
response = sms.send_message(recipient, sender, message)
```

The response will either be True or False depending on the outcome. 
