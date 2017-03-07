from django.conf.urls import url

#Model
from donor.models import Donor

#Views
from . import views

urlpatterns = [
    url(r'^donor/',views.donor_get_post,name="donor_api")
]