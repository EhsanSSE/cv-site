from django.urls import path
from mywebsite.views import *

urlpatterns = [
    path("", index_view),
    path('about', about_view),
    path('resume', resume_view),
    path('contact', contact_view)
]
