from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('user/', views.user, name='user'),
    path('delete/', views.delete, name='delete'),
]
