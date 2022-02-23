from django.db import models
from django.contrib.auth.models import AbstractUser


# Your models here.

class User(AbstractUser):
    pass


class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     ('Website', 'Website'),
    #     ('Youtube', 'Youtube'),
    #     ('Facebook', 'Facebook'),
    #     ('Instagram', 'Instagram'),

    # )
    first_name = models.CharField(max_length=50)  # first name field
    last_name = models.CharField(max_length=50)  # last name field
    email = models.EmailField(max_length=100)  # email field
    message = models.TextField()  # message field
    created_at = models.DateTimeField(auto_now_add=True)  # creation time field
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)  # agent field

    # phoned=models.BooleanField(default=False) #if user is contacted field
    # source=models.CharField(max_length=50, choices=SOURCE_CHOICES, default='Website') #source field
    # profile_picture=models.ImageField(upload_to='images/', blank=True,null=True) #profile pic field
    # special_files=models.FileField(upload_to='files/', blank=True,null=True) #special files field
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    # OneToOneField is a link to a user, only one user can be linked to an agent

    def __str__(self):
        return self.user.username
