from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ApplicationForm
from jobs.models import JobDetails
from django.contrib import messages
# Create your views here.
def apply(request,jobid):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        jobdata = JobDetails.objects.get(id=jobid)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.applied_for = jobdata
            new_record.save()
            messages.add_message(request, messages.INFO, 'Thanks For Applying '+str(jobdata.jobtitle)+'. Our recruiter will call you soon..')
            return HttpResponseRedirect('/')
    else:
        form = ApplicationForm
        jobdata = JobDetails.objects.get(id=jobid)
        print()
    return render(request,'apply.html',{'jobid':jobid,'form':form,'jobdata':jobdata})
