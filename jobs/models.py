from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class JobDetails(models.Model):
    jobtitle = models.CharField(max_length=200)
    jobdescription = models.CharField(max_length=2000)
    posted_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=datetime.now()+timedelta(days=30))

    def __str__(self):
        return self.jobtitle

    class Meta:
         verbose_name = "Job Detail"
