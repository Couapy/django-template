from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('create/<int:cz_id>/', views.create, name='create'),
    path('get/<int:id>/', views.get, name='get'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('like/<int:id>/', views.like, name='like'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
