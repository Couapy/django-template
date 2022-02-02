from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:id>/', views.CommentView.as_view(), name='comment'),
    path('comment/create/', views.CommentCreationView.as_view(), name='comment.create'),
]
