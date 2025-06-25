from django.contrib import admin
from .models import JobApplication, JobListing, Employee, Candidate

# Create job application Admin to display data in Admin site
class JobApplicationAdmin(admin.ModelAdmin):
    class Meta:
        model = JobApplication
        fields = '__all__'
admin.site.register(JobApplication,JobApplicationAdmin)
        
# Create job Listing Admin to display data in Admin site
class JobListingAdmin(admin.ModelAdmin):
    class Meta:
        model = JobListing
        fields = '__all__'
admin.site.register(JobListing,JobListingAdmin)

# Create Employee Admin to display data in Admin site
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee
        fields = '__all__'
admin.site.register(Employee, EmployeeAdmin)

# Create Candidate Admin to display data in Admin site
class CandidateAdmin(admin.ModelAdmin):
    class Meta:
        model = Candidate
        fields = '__all__'
admin.site.register(Candidate, CandidateAdmin)

