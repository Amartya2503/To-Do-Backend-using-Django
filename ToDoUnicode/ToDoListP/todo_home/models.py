from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class T_user(models.Model):

    id = models.IntegerField(primary_key = True)    
    name = models.CharField(max_length = 120, null = True)
    number = models.IntegerField( null= True, default = 0)
    email = models.CharField(max_length = 120, null= True)

    def __str__(self):
        return self.name


class todo(models.Model):

    use_by = models.ForeignKey(T_user, null = True,on_delete = models.CASCADE)
    task = models.CharField(max_length=122)
    time = models.IntegerField()
    category = models.CharField(max_length=122)
    count_id = models.IntegerField(default =0)
    status = models.BooleanField( default= 'False')

    def __str__(self):
        return self.task
