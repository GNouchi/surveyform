from django.conf.urls import url
from . import views
# this page matches the url 
urlpatterns = [
    url(r'^process$', views.process),
    url(r'^result$', views.result),
    url(r'^forceredirect$', views.forceredirect),    
    url(r'^', views.index),
]