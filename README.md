# simple-social-auth

### Simple Social Auth web app built with Django using social-auth-app-django library
---

```python
python manage.py migrate
python manage.py runserver 8000
```
--- 
### Add your API keys in settings.py
Note that this is for github, twitter, and facebook. If you want to add more go ahead.
```python
SOCIAL_AUTH_GITHUB_KEY = 'INSERT_PROVIDED_KEY_HERE'
SOCIAL_AUTH_GITHUB_SECRET = 'INSERT_PROVIDED_SECRET_HERE'

SOCIAL_AUTH_TWITTER_KEY = 'INSERT_PROVIDED_KEY_HERE'
SOCIAL_AUTH_TWITTER_SECRET = 'INSERT_PROVIDED_SECRET_HERE'

SOCIAL_AUTH_FACEBOOK_KEY = 'INSERT_PROVIDED_KEY_HERE' # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'INSERT_PROVIDED_SECRET_HERE' # App Secret

```