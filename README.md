```
- $ pipenv install django django-allauth django-environ
- $ pipenv shell
- $ django-admin startproject config .
- $ python manage.py startapp users
- créer User dans models.py, puis UserCreationForm et UserChangeForm, et UserAdmin
- settings.py:  INSTALLED_APPS = [
                    # ...
                    
                    'django.contrib.sites',

                    'allauth',
                    'allauth.account',
                    'allauth.socialaccount',
                    'allauth.socialaccount.providers.discord',

                    'users.apps.UsersConfig'
                ]

- config/settings.py: SITE_ID = 1
- config/settings.py: AUTH_USER_MODEL="users.User"
- config/settings.py:  from environ import Env
                env = Env()
                env.read_env(env_file=str(BASE_DIR / ".env"))
                DEBUG = env('DEBUG')
                SECRET_KEY = env('SECRET_KEY')
- https://discord.com/developers/applications/, puis New Application [https://gyazo.com/db89849c7661fa8fbcdd8d70477354ee]
- .env: DISCORD_CLIENT_ID=859323095714365451 et DISCORD_CLIENT_SECRET=s-k8d1MGC9FLXSIBLq4ZE3U2v5ySnyyJ
- ajouter la redirection: http://127.0.0.1:8000/accounts/discord/login/callback/
- config/urls.py: path("accounts/", include("allauth.urls"))
- $ python manage.py startapp users
- $ python manage.py migrate
- $ python manage.py createsuperuser

```