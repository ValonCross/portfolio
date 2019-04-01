from django.urls import path

# import blog.views
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    # Look for an int after the /blog and save as blog_id
    path('<int:blog_id>/', views.detail, name='detail'),
]