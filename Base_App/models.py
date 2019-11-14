from django.db import models

#importing django's inbuild User Model(username,password,email,email,etc) 
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #assign all User Data To user variable in One TO One Field
    user = models.OneToOneField(User,on_delete = models.CASCADE)


    #Additional Fields add in that User form
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to="profile_pic",blank=True)


    def __str__(self):
        return self.user.username