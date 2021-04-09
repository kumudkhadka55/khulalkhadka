from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.userregistration, name='signup'),
    path('login/', views.userlogin, name='login'),
]