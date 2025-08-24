from django.db import models

class Info(models.Model):
    # basic
    n_participants = models.IntegerField()
    n_officials = models.IntegerField()
    n_all = models.IntegerField()
    # users
    n_users = models.IntegerField()
    # search performance
    n_queries = models.IntegerField()
    n_displays = models.IntegerField()
    # date range
    start_date = models.DateField()
    end_date = models.DateField()
    # timestamps
    updated_at = models.DateField(auto_now=False)

    
    def __str__(self):
        return "Info for the statistics page"