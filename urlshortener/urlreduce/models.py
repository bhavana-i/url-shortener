from django.db import models
from  .urlreduce_utils import create_shortened_url

# Create your models here.

class Shortener(models.Model):
    '''
    This model creates a short url using the long url as the input
    created -> time and date the shortener was created
    times_followed = the number of times the shortened link has been followed
    short_url -> the shortened url
    long_url -> the original link
    '''

    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:

        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} shortened to {self.short_url}'


    def save(self, *args, **kwargs):

        if not self.short_url:

            self.short_url = create_shortened_url(self)
        
        super().save(*args, **kwargs)