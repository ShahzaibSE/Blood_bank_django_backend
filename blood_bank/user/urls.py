from django.conf.urls import url,include

#Views
from . import views

urlpatterns = [
    url(r'^user/',views.getallUsers,name="getUser")
]