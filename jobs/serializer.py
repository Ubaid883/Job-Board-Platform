from .models import JobApplication, JobListing
from rest_framework import serializers

# convert Job application complex data into json format 
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'

# convert Job Listing complex data into json format       
class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = '__all__'
        