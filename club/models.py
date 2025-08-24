from django.db import models


class Clubs(models.Model):
    name = models.CharField(max_length=100, unique=True)
    details = models.JSONField() # 元の構造を維持するため
    lastUpdated = models.DateField()

    def __str__(self):
        return self.name