from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="homePage"),
    path('login',views.login,name="loginPage")
]