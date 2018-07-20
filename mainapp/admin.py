from django.contrib import admin
from mainapp.models import JobApplication
# Register your models here.
class JobApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ['name','email','applied_for','phone_number','address','message','resume']
    list_display = ('name', 'email','applied_for','phone_number','status')
    def has_add_permission(self, request):
        return False

admin.site.register(JobApplication, JobApplicationAdmin)
