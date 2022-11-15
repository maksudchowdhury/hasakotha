
from django.db import models
#make sure you have added the app name in the installed app section of settings.py
# that is present inside the folder HasaKotha_core
# to create the models in the database first run the command inside the brackets [ python manage.py makemigrations ]
# next run this command inside the brackets [ python manage.py migrate ]

class user_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,blank=False, null=False)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=100,blank=False, null=False)
    nickname = models.CharField(max_length=50,blank=False, null=False)
    password = models.TextField(max_length=260,blank=False, null=False)
class user_message(models.Model):
    user_id = models.ForeignKey(user_info,on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=True)  