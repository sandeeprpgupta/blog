from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.TimeField(null=True,blank=True)
    user= models.ForeignKey(User,related_name="blog",on_delete=models.DO_NOTHING) #models.cascate --> will delete all user related 

    def __str__(self) -> str:
        return self.title
    


    