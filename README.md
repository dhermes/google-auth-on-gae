# `google-auth-on-gae`

To run the `dev_appserver`:

```
$ make app-run
```

and the main page should contain:

```python
>>> import google.auth
>>> scope = https://www.googleapis.com/auth/userinfo.email
>>> credentials, _ = google.auth.default(scopes=(scope,))
>>> credentials
<google.auth.app_engine.Credentials object at 0x7f7d7fab2910>
>>> credentials.token is None
True
>>>
>>> import google.auth.transport.requests
>>> request = google.auth.transport.requests.Request()
>>> credentials.refresh(request)
>>> credentials.token
'ya29.c.Eo0BEgWe...'
```
