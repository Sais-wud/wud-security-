from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),      
    path('signup/', views.signup, name='signup'),
]
