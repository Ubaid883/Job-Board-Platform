
from django.contrib import admin
from django.urls import path
from jobs.views import JobListingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/', JobListingView.as_view(), name='jobs'),

]
