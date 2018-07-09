#Dj Jot
##A basic implementation of JWT (JSON Web Tokens or "jot") via Django Rest Framework.

This isn't completely done, but has the basics there.

##Installation
Standard Django install:

1. Clone the repo and `cd` into the directory
2. `pip install -r requierments.txt`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
4. `python manage.py runserver`

##Available endpoints
For ease of use, you can hit these all from a browser.  Once authenticated, you should be able to see this all by going to `/api`

###users/actions/login
`POST` Go here first and log in with your superuser username and password.  You will need the JWT token that is returned in order to hit most other endpoints.

###users/
`GET` If you are authenticated you will be able to GET a list of all other users
`POST` If you are _not_ authenticated you should be able to POST a username, email, and password to create a user.

###users/{{ user_id }}
`GET` Return the information for the specified user

##Not implemented
1. users/actions/verify
But it would basically just be
```
if user.is_authenticated():
    return Response(status=200)
else:
    return Response(status=401)

2. The `PUT` and `PATCH` methods
3. Model validation

