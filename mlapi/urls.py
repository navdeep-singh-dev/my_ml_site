from django.urls import include, path
from . import views

# define the router
 
# define the router path and viewset to be used

urlpatterns = [
    path("", include("api.urls"))
]


