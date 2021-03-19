# AYTP Teaching and Learning Forum

This project is built on React as a frontend and Django rest framework api as a backend application.

## Project Build Process

The front end application is done with [React](https://github.com/facebook/create-react-app) and [Tailwind CSS](https://tailwindcss.com/docs/guides/create-react-app).
Resides in the frontend directory.

Using [Django REST framework](https://www.django-rest-framework.org/topics/documenting-your-api/) as the backend with simpleJWT, run the APIs on port [8000](http://localhost:8000)

Database used for the application is [Postgres](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

### Configurations in settings.py

Adding newly created applications
![](/screenshots/installed_apps.png).

Database configurations
![](/screenshots/database_config.png).

Other settings in [settings.py](elearn/settings.py)
![](/screenshots/other_settings.png).

### Configurations in [elearn/urls.py](elearn/urls.py)
![](/screenshots/urls_elearn.png).

## Testing APIs with Postman
Creating new user.
![](/screenshots/creating_user.JPG).

Output.
![](/screenshots/newuser_output.PNG).

Signing in with the new user credentials
![](/screenshots/sign_in.PNG).

API output tokens to signing in
![](/screenshots/api_signin_output.PNG).