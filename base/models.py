from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Chat(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    host=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="host")
    name=models.TextField(default="chat")
    
    def __str__(self):
        return self.name


class Messages(models.Model):
    body=models.TextField()
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    reciever=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reciever',null=True)
    chat=models.ForeignKey(Chat,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body
    

    



    
