from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('add/', views.add_data, name='add'),
    path('delete/<int:id>', views.delete_data, name='delete'),
    path('update/<int:id>', views.update_data, name='update'),
]
