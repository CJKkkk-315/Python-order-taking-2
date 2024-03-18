#from django.conf.urls import 
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "items"

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path(r'api/users^$', views.UserCreate.as_view(), name='account-create'),
    # path("register", views.register_request, name="register")
]

urlpatterns += staticfiles_urlpatterns()
