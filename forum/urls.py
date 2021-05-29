from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='forum-home'),
    path('topic/<int:pk>/', views.TopicDetailView.as_view(), name='topic-details'),
    path('topic/<int:pk>/add-post', views.PostCreateView.as_view(), name='add-post'),
    path('topic/<int:topic>/post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete-post'),
]