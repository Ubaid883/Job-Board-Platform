from django.shortcuts import render
from rest_framework import generics, filters
from .models import JobListing
from .serializer import JobListingSerializer

class JobListingView(generics.ListAPIView):
    queryset = JobListing.objects.filter(is_active=True)
    serializer_class = JobListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title','location','description']
# Create your views here.
