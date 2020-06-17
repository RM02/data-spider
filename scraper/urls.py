from django.urls import path
from scraper import views

urlpatterns = [
    path('getAll/', views.getAll)
    # path('getData/', views.getData)
]
