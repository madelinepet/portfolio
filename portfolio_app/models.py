from django.db import models


class News(models.Model):
    """ A class representing article data from the news.py API calls
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    source = models.CharField(max_length=200)
    date_published = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    dom_tone = models.CharField(max_length=300)
    image = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns a string representation of the News class
        """
        return f'Title: {self.title} | Description: {self.description} | Source: {self.source} | Published: {self.date_published} | Url: {self.url} | Tones: {self.dom_tone} | Image: {self.image} | Created: {self.created}'

    def __repr__(self):
        """ Returns a technical representation of the News class
        """
        return f'Title: {self.title} | Description: {self.description} | Source: {self.source} | Published: {self.date_published} | Url: {self.url} | Tones: {self.dom_tone} | Image: {self.image} | Created: {self.created}'
