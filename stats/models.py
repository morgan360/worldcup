from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    """List of teams in World Cup 2022"""
    name = models.CharField(max_length=128, help_text="The name of the Team.")
    group = models.CharField(max_length=1, help_text="Qualifying group")

    def __str__(self):
        return self.name


class Match(models.Model):
    date = models.DateField(verbose_name="Match Date")
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    phase = models.CharField(max_length=300)
    team1_score = models.IntegerField(default=0,
                                      validators=[MaxValueValidator(20), MinValueValidator(0)])
    team2_score = models.IntegerField(default=0,
                                      validators=[MaxValueValidator(20), MinValueValidator(0)])

    def winner(self):
        if self.team1_score > self.team2_score:
            return self.team1
        elif self.team1_score < self.team2_score:
            return self.team2
        elif self.team1_score == self.team2_score:
            return "draw"
        else:
            return "N/A"

    def __str__(self):
        return "%s %s %s" % (self.team1, " v ", self.team2)


class History(models.Model):
    """Matches Played between teams and ratios"""
    team1 = models.ForeignKey(Team, related_name='country1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='country2', on_delete=models.CASCADE)
    games = models.IntegerField()
    wins = models.FloatField()
    looses = models.FloatField()
    draws = models.FloatField()

    def __str__(self):
        return self.team1


class Fantasy(models.Model):
    match = models.ForeignKey(Match,  unique=True, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    score1 = models.IntegerField(default=0,                                validators=[MaxValueValidator(20), MinValueValidator(0)])
    score2 = models.IntegerField(default=0,
                                 validators=[MaxValueValidator(20), MinValueValidator(0)])

    def __str__(self):
        return "%s %s" % self.student


class Student(models.Model):
    """List of teams in World Cup 2022"""
    student = models.CharField(max_length=128, help_text="Student Name")
    year = models.CharField(max_length=5, help_text="What Class")

    def __str__(self):
        return self.student
