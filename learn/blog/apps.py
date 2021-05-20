from django.apps import AppConfig


class BlogConfig(AppConfig):#for django to recoznise our app as well the templates we need blogconfif in the list of installed apps
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
#the list of installed app are present in setting.py file of project.