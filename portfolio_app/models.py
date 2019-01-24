from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    """ A class representing article data from the news.py API calls
    """
    title = models.CharField(max_length=200, unique=True)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    source = models.CharField(max_length=200)
    date_published = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    dom_tone = models.CharField(max_length=300)

    def __str__(self):
        """ Returns a string representation of the News class
        """
        return f'Title: {self.title} |  Url: {self.url} | Description: {self.url} |Source: {self.source} | Published: {self.date_published} | Image: {self.image} |Tones: {self.dom_tone}'

    def __repr__(self):
        """ Returns a technical representation of the News class
        """
        return f'Title: {self.title} |  Url: {self.url} | Description: {self.url} |Source: {self.source} | Published: {self.date_published} | Image: {self.image} |Tones: {self.dom_tone}'


class Image(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='images'
    )
    url = models.CharField(max_length=180, default='Untitled')

    def __repr__(self):
        return f'<URL: {self.url}>'

    def __str__(self):
        return f'{self.url}'
