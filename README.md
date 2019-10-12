Docker Django
=============
A small Django application for managing users (CRUD) and their bank account information. This app is written with Django 2.2.5. This app was not created for production purposes.

Stack and version numbers used:

| Name                 | Version  |
|----------------------|----------|
| Django               | 2.2.5    |
| Postgresql           | 11.5     |
| Python               | 3.7.4    |

## Requirements
- Docker. See installation instructions at: [https://docs.docker.com/install/](https://docs.docker.com/install/)
- Docker Compose. See installation instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)


### Environment variables
The file `.env` contains the environment
variables needed in the containers. You can edit this as you see fit, and at
the moment these are the defaults that this project uses. However when you
intend to use this, keep in mind that you should keep this file out of version
control as it holds sensitive information regarding your project.


## Firing it up
Clone the project by executing the following command:
```
$ git clone git@github.com:apersan/django-bank-account-users.git
```

Start the container by issuing one of the following commands:
```bash
$ docker-compose up             # run in foreground
$ docker-compose up -d          # run in background
```

Now you can access the application at <http://0.0.0.0:8000/> and the admin site
at <http://0.0.0.0:8000/admin>.

A default admin user will be created for the Django Admin.
**Username:** admin
**Password:** admin

Once in the Django Admin, please go to http://0.0.0.0:8000/admin/password_change/ to change the password for this default user.

You can change other settings for this user under this page http://0.0.0.0:8000/admin/auth/user/1/change/

Once logged in, you can access the CRUD application by opening http://0.0.0.0:8000/ or clicking on *View Site*, on the top right corner of Django Admin.

![CRUD application](https://github.com/apersan/django-bank-account-users/raw/master/screenshots/list_of_users.png)

### Creating other admins
In this application, edit and delete operations on users are restricted to the admin who created them. Superadmin can perform all CRUD operations without any restriction.

In order to create other admin user, go to http://0.0.0.0:8000/admin/auth/user/ and click *Add User* on the top right corner. It is very important to tick the checkboxes *Active* and *Staff Status*. Otherwise, these users will not be able to access the CRUD application. If you tick *Superuser status*, this user will be have unrestricted access to any CRUD operation in this application.

In order to set up the right permissions for this new user, keep scrolling down until you see the User permissions section. Type *crud* in the filter. You should see 4 different permissions, which correspond to add, change, delete and view users on the CRUD application. Please assign them by moving them to the right panel.

![CRUD permissions](https://github.com/apersan/django-bank-account-users/raw/master/screenshots/crud_permissions.png "CRUD permissions")


### Google OAuth for Django Admin
If you want admins to be able to use their Google credentials to log in to the Django Admin, please follow open the settings.py file and paste your Google Client ID and Secret.

```python
# Google OAuth credentials
DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID = 'PASTE_HERE_YOUR_CLIENT_ID'
DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET = 'PASTE_HEREYOUR_CLIENT_SECRET'
```

In order to use log in with a Google Account, you must create first a new assignment between the user and its email account.

http://0.0.0.0:8000/admin/admin_sso/assignment/add/

Once the assignment has been created, the admin user will be able to log in with its Google account.

![Google Account Assignment](https://github.com/apersan/django-bank-account-users/raw/master/screenshots/google_account_assignment.png "Google Account Assignment")

