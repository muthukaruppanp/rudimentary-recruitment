from django.db import models
from jobs.models import JobDetails
from django.core.validators import RegexValidator

# Create your models here.
SELECTION_RESULT = (
   ('a', 'Accept/Shortlist'),
   ('r', 'Reject')
)
class JobApplication(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    applied_for = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    message = models.CharField(max_length=500,null=True,blank=True)
    resume = models.FileField(upload_to='resume/')
    status = models.CharField(choices=SELECTION_RESULT,null=True,blank=True, max_length=128)

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = "List of applicant"
