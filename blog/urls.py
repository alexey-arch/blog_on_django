from django.urls import path
from .views import BlogListView, BlogDetalView

urlpatterns = [
    path('post/<int:pk>/', BlogDetalView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]