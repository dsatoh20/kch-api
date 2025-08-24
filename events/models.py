from django.db import models


class Events(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    lastUpdated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} owned by {self.owner}"
    
class EventDates(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='date')
    date = models.DateField()

    def __str__(self):
        return f"{self.event.title} on {self.date}"