from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="messages")
    receiver=models.ForeignKey(User,on_delete=models.CASCADE)
    msg=models.TextField(max_length=10000)

    def __str__(self):
        return str(self.sender)+"   " +str(self.receiver)+"     "+self.msg
    