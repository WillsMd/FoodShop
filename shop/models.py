from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    phone_number = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    username = models.CharField()
    password = models.CharField()
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        
        return self.username, self.email
    
    class Meta:
        db_table = 'users'
    
