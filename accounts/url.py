from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
#    path('password/', views.Password.as_view(), name='password'),
]
