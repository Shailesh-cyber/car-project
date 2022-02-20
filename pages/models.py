from django.db import models


class Team(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    designation = models.CharField(max_length=500)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=500)
    twitter_link = models.URLField(max_length=500)
    google_plus_link = models.URLField(max_length=500)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstname

