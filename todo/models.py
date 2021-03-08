from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    
    text = models.TextField(blank=True)
    state = models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    