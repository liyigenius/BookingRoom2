from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from Booking import views
urlpatterns = patterns( '' ,
  #(r'^admin/', include('django.contrib.admin.urls')),
  (r'^accounts/', include('registration.urls')),
  (r'^$', views.hello),
)