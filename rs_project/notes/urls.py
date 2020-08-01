from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='notes-home'),
    path('addPost/', views.addPost),
    path('about/', views.about, name='notes-about'),
]


# looking for notes/post_list.html
# app/model_viewtype.html
