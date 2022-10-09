from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here

class Tournament(models.Model):
    name = models.TextField(max_length=100, help_text='Enter tournament name')
    description = models.TextField(max_length=200, help_text='Enter description tournament')
    logo = models.ImageField(default='none')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pass

    def __str__(self) -> str:
        return self.name

class Team(models.Model):
    name = models.TextField(max_length=100, help_text='Enter team name')
    logo = models.ImageField(default='none')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    players = models.ManyToManyField(User, through='Player')
    pass

    def __str__(self) -> str:
        return self.name

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teams = models.ForeignKey(Team, on_delete=models.CASCADE)
    pass

    def __str__(self) -> str:
        return self.user.first_name
