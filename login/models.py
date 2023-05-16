from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class login(models.Model):
#     username = models.CharField(max_length=200, null=False, unique=True)
#     email = models.CharField(max_length=200, null=False)
#     password = models.CharField(max_length=200, null=False)
#     # is_Manager = models.BooleanField(default=False)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
    
#     def __str__(self) -> str:
#         return self.username


class search(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=False)
    number = models.IntegerField(null=True)
    pos = models.IntegerField(null=True)
    nat = models.IntegerField(null=True)
    neg = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.title