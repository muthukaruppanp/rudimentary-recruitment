from django.shortcuts import render
from jobs.models import JobDetails
# Create your views here.
def index(request):
    jobdata = JobDetails.objects.all()
    return render(request, 'home.html',{'jobs':jobdata})
