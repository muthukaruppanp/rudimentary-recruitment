from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from jobs.models import JobDetails
from django import forms
# Register your models here.
class JobDetailForm( forms.ModelForm ):
    jobdescription = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = JobDetails
        fields = '__all__'

class JobDetailsAdmin(admin.ModelAdmin):
    form = JobDetailForm
    list_display = ('jobtitle', 'jobdescription','posted_date')
admin.site.register(JobDetails, JobDetailsAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
