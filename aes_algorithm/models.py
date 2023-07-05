from django.db import models

class UserData(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    
    def __str__(self):
        return f'self.username, self.email, self.password, self.salt'
    
