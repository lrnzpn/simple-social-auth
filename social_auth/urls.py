from . import views
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--

    # social auth management
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),
]
